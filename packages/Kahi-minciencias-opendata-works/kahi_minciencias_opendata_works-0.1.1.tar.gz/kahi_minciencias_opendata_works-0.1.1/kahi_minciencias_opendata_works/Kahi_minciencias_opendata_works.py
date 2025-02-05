from kahi.KahiBase import KahiBase
from pymongo import MongoClient, TEXT
from pymongo.errors import ConnectionFailure
from joblib import Parallel, delayed
from kahi_minciencias_opendata_works.process_one import process_one
from mohan.Similarity import Similarity


class Kahi_minciencias_opendata_works(KahiBase):

    config = {}

    def __init__(self, config):
        """
        Constructor for the Kahi_minciencias_opendata_works class.

        Several indices are created in the MongoDB collection to speed up the queries.
        We also handle the error to check db and collection existence.

        Parameters
        ----------
        config : dict
            The configuration dictionary. It should contain the following keys:
            - minciencias_opendata_works: a dictionary with the following keys:
                - task: the task to be performed. It can be "doi" or "all"
                - num_jobs: the number of jobs to be used in parallel processing
                - verbose: the verbosity level
                - database_url: the URL for the MongoDB database
                - database_name: the name of the database
                - collection_name: the name of the collection
                - es_index: the name of the Elasticsearch index
                - es_url: the URL for the Elasticsearch server
                - es_user: the username for the Elasticsearch server
                - es_password: the password for the Elasticsearch server
        """
        self.config = config

        self.mongodb_url = config["database_url"]

        self.client = MongoClient(self.mongodb_url)

        self.db = self.client[config["database_name"]]
        self.collection = self.db["works"]

        self.collection.create_index("authors.affiliations.id")
        self.collection.create_index("authors.id")
        self.collection.create_index([("titles.title", TEXT)])
        self.collection.create_index("external_ids.id")

        if "es_index" in config["minciencias_opendata_works"].keys() and "es_url" in config["minciencias_opendata_works"].keys() and "es_user" in config["minciencias_opendata_works"].keys() and "es_password" in config["minciencias_opendata_works"].keys():  # noqa: E501
            es_index = config["minciencias_opendata_works"]["es_index"]
            es_url = config["minciencias_opendata_works"]["es_url"]
            if config["minciencias_opendata_works"]["es_user"] and config["minciencias_opendata_works"]["es_password"]:
                es_auth = (config["minciencias_opendata_works"]["es_user"],
                           config["minciencias_opendata_works"]["es_password"])
            else:
                es_auth = None
            self.es_handler = Similarity(
                es_index, es_uri=es_url, es_auth=es_auth)
            print("INFO: ES handler created successfully")
        else:
            self.es_handler = None
            print("WARNING: No elasticsearch configuration provided")

        self.task = config["minciencias_opendata_works"]["task"] if "task" in config["minciencias_opendata_works"].keys(
        ) else None
        self.insert_all = config["minciencias_opendata_works"]["insert_all"] if "insert_all" in config["minciencias_opendata_works"].keys(
        ) else False
        self.thresholds = config["minciencias_opendata_works"]["thresholds"] if "thresholds" in config["minciencias_opendata_works"].keys(
        ) else None
        self.n_jobs = config["minciencias_opendata_works"]["num_jobs"] if "num_jobs" in config["minciencias_opendata_works"].keys(
        ) else 1
        self.verbose = config["minciencias_opendata_works"]["verbose"] if "verbose" in config["minciencias_opendata_works"].keys(
        ) else 0

        # checking if the databases and collections are available
        self.check_databases_and_collections()

    def check_databases_and_collections(self):
        """
        Method to check if the databases and collections are available.
        """
        try:
            with MongoClient(self.config["minciencias_opendata_works"]["database_url"]) as client:
                db_name = self.config["minciencias_opendata_works"]["database_name"]
                collection_name = self.config["minciencias_opendata_works"]["collection_name"]

                # Check if database exists
                if db_name not in client.list_database_names():
                    raise ValueError(f"Database {db_name} not found")

                db = client[db_name]

                # Check if collection exists
                if collection_name not in db.list_collection_names():
                    raise ValueError(
                        f"Collection {collection_name} in database {db_name} not found")

        except ConnectionFailure:
            raise ConnectionFailure("Failed to connect to MongoDB server.")

    def process_opendata(self):
        """
        Method to process the minciencias_opendata database.
        Checks if the task is "doi" or "all" and processes the records accordingly.
        """
        client = MongoClient(
            self.config["minciencias_opendata_works"]["database_url"])
        db = client[self.config["minciencias_opendata_works"]["database_name"]]
        opendata = db[self.config["minciencias_opendata_works"]
                      ["collection_name"]]
        print("INFO: Creating indices")
        opendata.create_index("id_producto_pd")
        opendata.create_index("nme_tipologia_pd")
        if self.task == "doi":
            raise RuntimeError(
                f'''{self.config["minciencias_opendata_works"]["task"]} is not a valid task for the minciencias_opendata database''')

        # bibliography production requires a search in elasticsearch,
        # there will be a cut in openalex for those products.
        biblio = ["Publicaciones editoriales no especializadas",
                  "Notas científica",
                  "Informe Final de Investigación",
                  "Capítulos de libro de investigación",
                  "Libros de investigación",
                  "Artículos de investigación",
                  "Libros de Formación",
                  "Libros",
                  "Tesis de doctorado",
                  "Capítulos de libro",
                  "Documento de trabajo",
                  "Tesis de pregrado",
                  "Informe técnico final",
                  "Artículos",
                  "Manuales y Guías Especializadas",
                  "Boletín divulgativo de resultado de investigación",
                  "Libros de Divulgación de investigación y/o Compilación de Divulgación",
                  "Tesis de maestria",
                  "Generación de contenido impresa"]

        pipeline = [
            {'$match': {"nme_producto_pd": {"$exists": True}}},
            {'$match': {'nme_tipologia_pd': {'$in': biblio}}},
            {'$group': {'_id': '$id_producto_pd', 'originalDoc': {'$first': '$$ROOT'}}},
            {'$replaceRoot': {'newRoot': '$originalDoc'}}
        ]
        paper_list = list(opendata.aggregate(pipeline, allowDiskUse=True))
        print(
            f"INFO: Processing bibliographic production {len(paper_list)} catgories {biblio}")
        Parallel(
            n_jobs=self.n_jobs,
            verbose=self.verbose,
            backend="threading")(
            delayed(process_one)(
                work,
                self.db,
                self.collection,
                self.empty_work(),
                self.es_handler,
                insert_all=self.insert_all,
                thresholds=self.thresholds,
                verbose=self.verbose
            ) for work in paper_list
        )
        client.close()

    def run(self):
        self.process_opendata()
        return 0
