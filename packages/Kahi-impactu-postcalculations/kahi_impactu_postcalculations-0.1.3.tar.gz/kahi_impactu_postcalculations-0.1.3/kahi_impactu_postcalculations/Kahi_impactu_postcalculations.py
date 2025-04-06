from joblib import Parallel, delayed
from kahi.KahiBase import KahiBase
from pymongo import MongoClient
import subprocess
from spacy import cli, load
from kahi_impactu_postcalculations.process_one import network_creation_process_one, top_words_process_one, count_works_one, load_nlp_models
from kahi_impactu_postcalculations.indexes import create_indexes
from kahi_impactu_postcalculations.denormalization import denormalize


class Kahi_impactu_postcalculations(KahiBase):
    """
    Plugin for performing post calculations for Impactu.

    This class extends KahiBase and implements functions for creating co-authorship networks and
    extracting top words
    """

    config = {}

    def __init__(self, config):
        """
        Initialize the Kahi_impactu_postcalculations plugin.
        """
        self.config = config

        self.mongodb_url = config["database_url"]
        self.database_name = config["database_name"]

        self.impactu_database_url = config["impactu_postcalculations"]["database_url"]
        self.impactu_database_name = config["impactu_postcalculations"]["database_name"]
        self.backend = self.config["impactu_postcalculations"]["backend"]
        self.verbose = self.config["impactu_postcalculations"]["verbose"]
        self.n_jobs = self.config["impactu_postcalculations"]["n_jobs"]
        self.author_count = self.config["impactu_postcalculations"][
            "author_count"] if "author_count" in self.config["impactu_postcalculations"] else 6
        self._check_and_install_spacy_models()

    def _check_and_install_spacy_models(self):
        """
        Check if the spaCy models are installed and install them if needed.
        """
        print("INFO: Checking spaCy models")
        if not self.are_spacy_models_installed():
            print("INFO: Installing spaCy models")
            self.install_spacy_models()
        self.en_model = load('en_core_web_sm')
        self.es_model = load('es_core_news_sm')
        self.stopwords = self.en_model.Defaults.stop_words.union(
            self.es_model.Defaults.stop_words)
        # Load the spaCy models in process one for parallel computing
        load_nlp_models()

    def are_spacy_models_installed(self):
        """
        Check if the required spaCy models are installed.

        Returns:
            bool: True if models are installed, False otherwise.
        """
        return "en_core_web_sm" in cli.info()["pipelines"].keys() and "es_core_news_sm" in cli.info()["pipelines"].keys()

    def install_spacy_models(self):
        """
        Install the required spaCy models.
        """
        subprocess.run(["python3", "-m", "spacy",
                       "download", "en_core_web_sm"])
        subprocess.run(["python3", "-m", "spacy",
                       "download", "es_core_news_sm"])

    def run(self):
        """
        Execute the plugin to create co-authorship networks and extract top words.
        """

        client = MongoClient(self.mongodb_url)
        db = client[self.database_name]

        impactu_client = MongoClient(self.impactu_database_url)

        client = MongoClient(self.mongodb_url)
        db = client[self.database_name]

        print(f"INFO: Creating indexes in db {self.database_name} for backend")
        db["works"].create_index("authors.id")
        create_indexes(db)

        print(f"INFO: Denormalizing data in {self.database_name}.works")
        denormalize(db.works)

        # Getting the list of institutions ids with works
        print("INFO: Getting authors and affiliations ids")
        institutions_ids = []
        for aff in db["affiliations"].find({"types.type": {"$nin": ["faculty", "department", "group"]}}, {"_id": 1}):
            count = db["works"].count_documents(
                {"authors.affiliations.id": aff["_id"]})
            if count != 0:
                institutions_ids.append(aff["_id"])

        # Creating the networks of coauthorship for each affiliation
        print("INFO: Creating affiliations networks")
        if institutions_ids:
            Parallel(
                n_jobs=self.n_jobs,
                verbose=10,
                backend=self.backend)(
                    delayed(network_creation_process_one)(
                        self.config,
                        client if self.backend == "threading" else None,
                        impactu_client if self.backend == "threading" else None,
                        idx,
                        self.author_count,
                        "affiliations",
                        self.backend
                    ) for idx in institutions_ids)

        # Getting the list of authors ids with works
        print("INFO: Checking authors with works")
        authors_ids = [x["_id"] for x in db["person"].find({}, {"_id": 1})]

        # this could be threads, is a basic thing.
        authors_ids = Parallel(n_jobs=self.n_jobs, backend="threading", verbose=1)(
            delayed(count_works_one)(
                db,
                author
            ) for author in authors_ids)

        # remove Nones
        authors_ids = [x for x in authors_ids if x is not None]

        print(f"INFO: total authors {len(authors_ids)}")
        # Creating the networks of coauthorship for each author
        print("INFO: Creating authors networks")
        if authors_ids:
            Parallel(
                n_jobs=self.n_jobs,
                verbose=10,
                backend=self.backend)(
                    delayed(network_creation_process_one)(
                        self.config,
                        client if self.backend == "threading" else None,
                        impactu_client if self.backend == "threading" else None,
                        idx,
                        self.author_count,
                        "person",
                        self.backend
                    ) for idx in authors_ids)
        # Getting the top words for each institution
        print("INFO: Creating top words for institutions")
        affiliations_cursor = list(db["affiliations"].find({}, {"_id": 1}))
        Parallel(
            n_jobs=self.n_jobs,
            verbose=10,
            backend=self.backend)(
                delayed(top_words_process_one)(
                    self.config,
                    client if self.backend == "threading" else None,
                    impactu_client if self.backend == "threading" else None,
                    aff,
                    self.stopwords,
                    "affiliations",
                    self.backend
                ) for aff in affiliations_cursor)

        # Getting the top words for others organizations
        print("INFO: Creating top words for others affiliations such as faculty, department, group")
        affiliations_cursor = list(db["affiliations"].find(
            {"types.type": {"$in": ["faculty", "department", "group"]}}, {"_id": 1}))
        Parallel(
            n_jobs=self.n_jobs,
            verbose=10,
            backend=self.backend)(
                delayed(top_words_process_one)(
                    self.config,
                    client if self.backend == "threading" else None,
                    impactu_client if self.backend == "threading" else None,
                    aff,
                    self.stopwords,
                    "affiliations",
                    self.backend
                ) for aff in affiliations_cursor)

        # Getting the top words for each author
        print("INFO: Creating top words for person")
        authors_cursor = list(db["person"].find({}, {"_id": 1}))

        Parallel(
            n_jobs=self.n_jobs,
            verbose=10,
            backend=self.backend)(
                delayed(top_words_process_one)(
                    self.config,
                    client if self.backend == "threading" else None,
                    impactu_client if self.backend == "threading" else None,
                    author,
                    self.stopwords,
                    "person",
                    self.backend
                ) for author in authors_cursor)
