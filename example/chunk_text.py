"""
Example script in order to convert a pdf to images.
"""
# Libraries
import os

import pandas as pd

# Globals
DIR_ROOT = "/Users/temp-admin/repositories/ollama_sandbox"
DIR_DATA = os.path.join(DIR_ROOT, 'data')
DIR_TEXT = os.path.join(DIR_DATA, 'text')
DIR_CHUNKS = os.path.join(DIR_DATA, 'chunks')
FILE_NAME = "filing.txt"

# Load File
with open(os.path.join(DIR_TEXT, FILE_NAME), 'r') as f:
    text = f.read()

# File Length
num_tokens = 500
tokens = text.split(" ")
total_tokens = len(tokens)

# Chunk Text
chunks = []
chunk_ids = []
count = 0

print("Chunking text")
for i in range(0, total_tokens, num_tokens):
    count += 1
    chunk_ids.append(count)
    chunks.append(" ".join(tokens[i:i + num_tokens]))
    print(f"\tCreating chunk from {i } to {i + num_tokens}")

print("Creating chunk dataframe")
chunk_df = pd.DataFrame({"chunk_ids": chunk_ids, "chunks": chunks})

print(f"Writing chunk dataframe to {DIR_CHUNKS}")
chunk_df.to_csv(os.path.join(DIR_CHUNKS, "chunks.csv"))
print("Script completed")
