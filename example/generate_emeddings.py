import os
import pandas as pd
from fastembed import TextEmbedding
from typing import List

# Globals
DIR_DATA = "/Users/temp-admin/repositories/ollama_sandbox/data"
DIR_CHUNKS = os.path.join(DIR_DATA, "chunks")
DIR_EMBEDDINGS = os.path.join(DIR_DATA, "embeddings")
FILE_NAME = "chunks.parquet"

# Load File
path = os.path.join(DIR_CHUNKS, FILE_NAME)
chunk_df = pd.read_parquet(path)

# Model
model = TextEmbedding()

# Generate Embeddings
print("Generating Embeddings")
chunk_df['embeddings'] = list(
    map(
        lambda x: list(model.embed(x))[0].tolist(),
        chunk_df['chunk_text'].values
    )
)


# Write Embeddings to file
path = os.path.join(DIR_EMBEDDINGS, "embeddings.parquet")
print(f"Writing file to {path}")
chunk_df.to_parquet(path)

print("Script finished")




