import os
import re
import pandas as pd
import ollama
from src.retrieval import RetrievalCosine

# Globals
DIR_DATA = "/Users/temp-admin/repositories/ollama_sandbox/data"
DIR_EMBEDDINGS = os.path.join(DIR_DATA, "embeddings")                              
FILE_NAME = "embeddings.parquet"                                             
                                                                                   
# Load Data                                                                        
chunk_df = pd.read_parquet(                                                        
    path=os.path.join(DIR_EMBEDDINGS, FILE_NAME),                                  
    columns=["chunk_id", "chunk_text", "embeddings"],                                 
)  

# User Query
query = "Total number of employees in 2021"
task = "Return the total number of employees employed by Ford Motor in 2021"
example = "employees: 100"

# Get Nearest
n_matches = 5
context = RetrievalCosine(
    data=chunk_df,
    embedding_col="embeddings",
    text_col="chunk_text",
    n_matches=n_matches,
).get_nearest_match(query)


# Create Prompt
print("Executing first request")
role = "user"
prompt = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Today Date: 26 Jul 2024

You are a helpful Assistant.<|eot_id|><|start_header_id|>user<|end_header_id|>

Here is a piece of text {}.
Please {}.
Return your answer in json format.
Here is an example {}.

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
""".format("\n".join(context), task, example)

messages = [{'role': role, 'content': prompt}]

response = ollama.generate(
        model='llama3.1',
        prompt=prompt,
)
content = response['response']

print(content)

