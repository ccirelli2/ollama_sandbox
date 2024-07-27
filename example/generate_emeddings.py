from fastembed import TextEmbedding
from typing import List

# Example list of documents
documents: List[str] = [
    "This is built to be faster and lighter than other embedding libraries e.g. Transformers, Sentence-Transformers, etc.",
    "fastembed is supported by and maintained by Qdrant.",
]

# This will trigger the model download and initialization
embedding_model = TextEmbedding()
print("The model BAAI/bge-small-en-v1.5 is ready to use.")

embeddings_generator = embedding_model.embed(documents)  # reminder this is a generator
embeddings_list = list(embedding_model.embed(documents))



