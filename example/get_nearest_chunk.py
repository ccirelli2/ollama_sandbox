"""
Calculate the nearest chunk to query
"""

import os

import pandas as pd
from src.retrieval import RetrievalCosine

# Globals
DIR_ROOT = "/Users/temp-admin/repositories/ollama_sandbox"
DIR_DATA = os.path.join(DIR_ROOT, 'data')
DIR_CHUNKS = os.path.join(DIR_DATA, 'chunks')
DIR_EMBEDDINGS = os.path.join(DIR_DATA, "embeddings")
FILE_NAME = "chunk_embeddings.parquet"

# Load Data
use_cols = []
chunk_df = pd.read_parquet(
    path=os.path.join(DIR_EMBEDDINGS, FILE_NAME),
    columns=["chunk_ids", "chunks", "embeddings"],
)

# Create Query
"""
query = "Ford annual revenues"
text = "Today is a good day to code"

# Embed Query
model = TextEmbedding()
q_embedding = list(model.embed(query))[0]
t_embedding = list(model.embed(text))[0]

# Calculate Distance Between Query & All Chunks
chunk_df['distance'] = list(
    map(lambda x: np.dot(x, q_embedding), chunk_df['embeddings']))

# Get Top Matches
chunk_df.sort_values(by="distance", ascending=False, inplace=True)

# Return Text Top Matches
num_matches = 5
top_matches = chunk_df['chunks'].head(num_matches).values.tolist()
"""

if __name__ == "__main__":
    fetcher = RetrievalCosine(
        data=chunk_df,
        embedding_col="embeddings",
        text_col="chunks",
    )

    query = "Ford Motor Company Annual Revenues"
    nearest_matches = fetcher.get_nearest_match(query=query)

    print(nearest_matches[0])
