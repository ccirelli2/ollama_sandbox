import os
import pandas as pd
import ollama
from src.retrieval import RetrievalCosine

# Globals
DIR_DATA = "/Users/temp-admin/repositories/ollama_sandbox/data"
DIR_EMBEDDINGS = os.path.join(DIR_DATA, "embeddings")                              
FILE_NAME = "chunk_embeddings.parquet"                                             
                                                                                   
# Load Data                                                                        
chunk_df = pd.read_parquet(                                                        
    path=os.path.join(DIR_EMBEDDINGS, FILE_NAME),                                  
    columns=["chunk_ids", "chunks", "embeddings"],                                 
)  

# User Query
query = "2020 annual revenues"

# Get Nearest
n_matches = 2
context = RetrievalCosine(
    data=chunk_df,
    embedding_col="embeddings",
    text_col="chunks",
    n_matches=n_matches,
).get_nearest_match(query)


# Create Prompt
role = "user"
prompt = """
You are a assistant tasked with retrieving data from bodies of text.

You will be provided with a body text contained within tags <content>text</content>.

Your jobs is to extract the total annual revenues in US dollar.

<content>{}</content>

Only respond with the requested attribute.  If you cannot find the attribute
please reponse with 'value not found'.
""".format(context)
messages = [{'role': role, 'content': prompt}]
response = ollama.chat(model='llama3.1', messages=messages)

print(response)








