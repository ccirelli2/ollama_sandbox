"""
Example script in order to convert a pdf to images.
"""
# Libraries
import os

import pandas as pd
from fastembed import TextEmbedding

# Globals
DIR_ROOT = "/Users/temp-admin/repositories/ollama_sandbox"
DIR_DATA = os.path.join(DIR_ROOT, 'data')
DIR_CHUNKS = os.path.join(DIR_DATA, 'chunks')
DIR_EMBEDDINGS = os.path.join(DIR_DATA, "embeddings")
FILE_NAME = "chunks.csv"

# Load Chunk Dataframe
chunk_df = pd.read_csv(os.path.join(DIR_CHUNKS, FILE_NAME))

# Instantiate Embedding Model
print("Creating embeddings")
documents = chunk_df['chunks'].values.tolist()
embedding_model = TextEmbedding()
embeddings_list = list(embedding_model.embed(documents))

# Add Embeddings to Dataframe
chunk_df['embeddings'] = [i.tolist() for i in embeddings_list]

# Write Embeddings to file
print("Writing embeddings to file")
chunk_df.to_parquet(os.path.join(DIR_EMBEDDINGS, 'chunk_embeddings.parquet'))
print("Script finished")
