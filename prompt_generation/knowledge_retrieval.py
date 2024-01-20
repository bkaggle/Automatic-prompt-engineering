import logging

from config import THRESHOLD, LOW_CONFIDENCE
from vector_store import VectorStore


class KnowledgeRetrieval:
    def __init__(self, knowledge, refresh=False):
        # I instantiate a Vector Store class (in this case with FAISS)
        self.vector_store = VectorStore()

        # Then, my documents are stored (if they were not)
        self.vector_store.index_array(knowledge, refresh=refresh)

    def retrieve(self, prompt):
        logging.info(f"QUESTION: {prompt}")
        logging.info("RETRIEVED>>")
        res = self.vector_store.knowledge_retrieval(prompt)

        knowledge_elements = []
        for r in res:
            logging.info(f"- [{r[1] if r[1] < THRESHOLD else LOW_CONFIDENCE}]: {r[0].page_content}]")
            if r[1] < THRESHOLD:
                knowledge_elements.append(r[0].page_content)

        knowledge = "\n".join(knowledge_elements)
        logging.info(f"COMBINED KNOWLEDGE>>\n{knowledge}")

        return knowledge