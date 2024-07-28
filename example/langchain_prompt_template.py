"""
"""
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate




prompt = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{ system_prompt }<|eot_id|><|start_header_id|>user<|end_header_id|>

{ user_msg_1 }<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{{ model_answer_1 }}<|eot_id|>
"""
