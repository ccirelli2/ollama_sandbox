import ollama

role = "user"
text = """
Ford Motor Company (commonly known as Ford) is an American multinational
automobile manufacturer headquartered in Dearborn, Michigan, United States.
It was founded by Henry Ford and incorporated on June 16, 1903.
The company sells automobiles and commercial vehicles under the Ford brand,
and luxury cars under its Lincoln brand. The company is listed on the
New York Stock Exchange and is controlled by the Ford family; they have
minority ownership but the majority of the voting power.
"""

content = """
You will be provided with a piece of text.  It will be contained within tags
<content>text</content>.

Your jobs is to extract the date on which the company was incorporated.
Your response should be formatted as Month/Day/Year.

Please find below the text
<content>{}</content>

Please return your response in json format.
""".format(text)
messages = [{'role': role, 'content': content}]
response = ollama.chat(model='llama3', messages=messages)

print(response['message']['content'])
