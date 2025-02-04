from kahi.KahiBase import KahiBase
from pymongo import MongoClient, TEXT
from joblib import Parallel, delayed

from mohan.Similarity import Similarity
from kahi_scholar_works.process_one import process_one


class Kahi_scholar_works(KahiBase):

    config = {}

    def __init__(self, config):
        """
        Constructor for the Kahi_scholar_works class.

        Several indices are created in the database to speed up the process.
        We also handle the error to check db and collection existence.

        Parameters:
        -----------
        config : dict
            The configuration dictionary. It should contain the following keys:
            - scholar_works: A dictionary with the following keys:
                - database_url: The url of the scholar works database.
                - database_name: The name of the scholar works database.
                - collection_name: The name of the collection in the scholar works database.
                - task: The task to be performed. It can be "doi" or empty for similarity.
                - num_jobs: The number of jobs to be used in parallel processing.
                - verbose: The verbosity level.
                - es_index: The index to be used in elasticsearch.
                - es_url: The url of the elasticsearch server.
                - es_user: The user for the elasticsearch server.
                - es_password: The password for the elasticsearch server.
        """
        self.config = config

        self.mongodb_url = config["database_url"]

        self.client = MongoClient(self.mongodb_url)

        self.db = self.client[config["database_name"]]
        self.collection = self.db["works"]

        self.collection.create_index("external_ids.id")
        self.collection.create_index("year_published")
        self.collection.create_index("authors.affiliations.id")
        self.collection.create_index("authors.id")
        self.collection.create_index([("titles.title", TEXT)])

        self.scholar_client = MongoClient(
            config["scholar_works"]["database_url"])
        if config["scholar_works"]["database_name"] not in self.scholar_client.list_database_names():
            raise ValueError(
                f"Database {config['scholar_works']['database_name']} not found in {config['scholar_works']['database_url']}")
        self.scholar_db = self.scholar_client[config["scholar_works"]
                                              ["database_name"]]
        if config["scholar_works"]["collection_name"] not in self.scholar_db.list_collection_names():
            raise ValueError(
                f"Collection {config['scholar_works']['database_name']}.{config['scholar_works']['collection_name']} not found in {config['scholar_works']['database_url']}")
        self.scholar_collection = self.scholar_db[config["scholar_works"]
                                                  ["collection_name"]]

        if "es_index" in config["scholar_works"].keys() and "es_url" in config["scholar_works"].keys() and "es_user" in config["scholar_works"].keys() and "es_password" in config["scholar_works"].keys():
            es_index = config["scholar_works"]["es_index"]
            es_url = config["scholar_works"]["es_url"]
            if config["scholar_works"]["es_user"] and config["scholar_works"]["es_password"]:
                es_auth = (config["scholar_works"]["es_user"],
                           config["scholar_works"]["es_password"])
            else:
                es_auth = None
            self.es_handler = Similarity(
                es_index, es_uri=es_url, es_auth=es_auth)
        else:
            self.es_handler = None
            print("WARNING: No elasticsearch configuration provided")

        self.task = config["scholar_works"]["task"]
        self.n_jobs = config["scholar_works"]["num_jobs"] if "num_jobs" in config["scholar_works"].keys(
        ) else 1
        self.verbose = config["scholar_works"]["verbose"] if "verbose" in config["scholar_works"].keys(
        ) else 0

    def process_scholar(self):
        """
        Method to process the scholar works, and add them to the main database.

        We use the process_one function to process each paper in parallel.

        There are to possible tasks:
        - "doi": process papers with doi
        - empty to process papers without doi using similarity with Mohan package (https://github.com/colav/Mohan)
        The task is defined in the configuration file. (Read more about tasks in Mohan package)
        """
        # selects papers with doi according to task variable
        if self.task == "doi":
            paper_cursor = self.scholar_collection.find(
                {"$and": [{"doi": {"$ne": ""}}, {"doi": {"$ne": None}}]})
        else:
            paper_cursor = self.scholar_collection.find(
                {"$or": [{"doi": {"$eq": ""}}, {"doi": {"$eq": None}}]})

        client = MongoClient(self.mongodb_url)
        db = client[self.config["database_name"]]
        collection = db["works"]
        Parallel(
            n_jobs=self.n_jobs,
            verbose=self.verbose,
            backend="threading")(
            delayed(process_one)(
                paper,
                db,
                collection,
                self.empty_work(),
                False if self.task == "doi" else True,
                es_handler=self.es_handler,
                verbose=self.verbose
            ) for paper in paper_cursor
        )
        client.close()

    def run(self):
        """
        Method start the execution of the workflow in parallel.
        """
        self.process_scholar()
        return 0
