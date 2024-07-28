"""
Example script in order to convert a pdf to images.
"""
# Libraries
import os
import pandas as pd
from src.splitters import TextSplitterByToken

# Globals
DIR_ROOT = "/Users/temp-admin/repositories/ollama_sandbox"
DIR_DATA = os.path.join(DIR_ROOT, 'data')
DIR_TEXT = os.path.join(DIR_DATA, 'text')
DIR_CHUNKS = os.path.join(DIR_DATA, "chunks")

# Get Page Filenames
pages = os.listdir(DIR_TEXT)
chunks_all = []
ids_all = []
page_num_all = []
file_names_all = []
char_count_all = []


for p in pages:
    print(f"Creating chunks for file {p}")
    # Load Example Text File
    file_name = p
    page_num = file_name.replace(".text", "").replace("page", "")
    path = os.path.join(DIR_TEXT, file_name)
    
    # Load Text File
    with open(path, 'r') as f:
        text = f.read()

    # Chunk Text
    splitter = TextSplitterByToken(separator=" ", num_tokens=200)
    chunks = splitter.split_text(text)

    # Create Chunk Ids
    def add_one(num):
        return num + 1
    chunk_ids = [add_one(i) for i in range(len(chunks))]

    # Page Numbers
    page_numbers = [page_num for i in range(len(chunks))]

    # File name
    file_names = [file_name for file_name in range(len(chunks))]
   
    # Get Char Count
    char_count = [len(c) for c in chunks]

    # Append Results
    chunks_all += chunks
    ids_all += chunk_ids
    page_num_all += page_numbers
    file_names_all += file_names
    char_count_all += char_count
    

# Create DataFrame
print("Creating chunk dataframe")
chunk_df = pd.DataFrame({
    "file_name": file_names_all,
    "page_number": page_num_all,
    "chunk_id": ids_all,
    "chunk_text": chunks_all,
    "char_count": char_count_all,
})


print(f"Writing chunk dataframe to => {DIR_CHUNKS}")
chunk_df.to_parquet(os.path.join(DIR_CHUNKS, "chunks.parquet"))















