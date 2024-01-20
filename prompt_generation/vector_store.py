import logging
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import config


class VectorStore:
    def __init__(self):
        self.db = None
        

    def index_array(self, array, refresh=False):
        embeddings = OpenAIEmbeddings()
        if not refresh:
            try:
                self.db = FAISS.load_local(config.STORE_PATH, embeddings)
                logging.info("Embeddings cached. Loading...")
            except:
                logging.info("Cache clean.")

        if self.db is None:
            logging.info("Generating embeddings with OpenAI...")
            self.db = FAISS.from_texts(array, embeddings)
            logging.info(f"Saving embeddings into {config.STORE_PATH}")
            self.db.save_local(config.STORE_PATH)

    def knowledge_retrieval(self, prompt):
        return self.db.similarity_search_with_score(prompt)