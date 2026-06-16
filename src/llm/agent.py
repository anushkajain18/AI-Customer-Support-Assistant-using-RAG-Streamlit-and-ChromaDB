import chromadb
from dotenv import load_dotenv

load_dotenv()


class CustomerSupportAgent:

    def __init__(self):

        # ChromaDB client
        self.chroma_client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        # Collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="support_docs"
        )

    async def initialize(self):

        documents = [
            "Customers can return products within 30 days.",
            "Shipping usually takes 5 to 7 business days.",
            "Warranty is valid for 1 year.",
            "Refunds are processed within 5 business days."
        ]

        ids = [f"id{i}" for i in range(len(documents))]

        # Add only once
        if self.collection.count() == 0:

            self.collection.add(
                documents=documents,
                ids=ids
            )

    async def _rag_search(self, query: str):

        results = self.collection.query(
            query_texts=[query],
            n_results=2
        )

        docs = results["documents"][0]

        return "\n".join(docs)

    async def process_query(self, query: str):

        # Get context from RAG
        context = await self._rag_search(query)

        # Return local response without OpenAI API
        return f"""
Customer Support Response:

{context}
"""
