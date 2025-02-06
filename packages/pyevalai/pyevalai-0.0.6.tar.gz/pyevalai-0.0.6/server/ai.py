import requests
import re
from jinja2 import Environment, FileSystemLoader
from IPython.display import display, Markdown

# Setzen Sie Ihren API-Schlüssel hier ein
API_KEY = "YOUR_API_KEY"




# URL des lokalen API-Endpunkts
#URL = "http://localhost:5000/v1/completions"
URL = "http://localhost:5001/v1/completions"

environment = Environment(loader=FileSystemLoader("server/instruction-templates/"))
template = environment.get_template("Mistral.yaml") # Mistral model
#template = environment.get_template("Llama-v3.yaml") # LLAMA model
#template = environment.get_template("DeepSeek LLama.yaml") # LLAMA model
ai_author = "Mistral_large" # this name will be used to specify the author of grades

headers = {
	"Content-Type": "application/json",
	"Authorization": f"Bearer {API_KEY}"
}

def ask(prompt,max_tokens=10000):
	payload = {
		"prompt": prompt,
		"max_tokens": max_tokens,
		"stop": ["[INST]"],
		"seed":0,
		"temperature":0 # damit antworten deterministisch werden
	}
	
	response = requests.post(URL, headers=headers, json=payload)
	
	if response.status_code == 200:
		return response.json()["choices"][0]["text"]
	else:
		print(f"Fehler: {response.status_code}")
		print(response.text)

def msg(content,role="user"):
	return [{"role":role,"content":content}]

def chat(messages,answer_start="",max_tokens=10000,display_chat=None):
	"""
	:messages: list of msg(role,content) entries
	:answer_start: beginning of answer
	:max_tokens: maximum number of tokens for reply
	:display_chat: if True: display entire chat. if number: display last n chat messages (including reply)
	"""# TODO: add: display-parameter => soll dann neuen chat zeigen
	prompt = template.render(messages=messages)
	answer = ask(prompt+answer_start,max_tokens = max_tokens)
	answer = latex_escape(answer_start+answer) # escape latex commands for markdown
	messages = messages + msg(answer,"assistant")
	return messages

def latex_escape(text):
	return text.replace("\\(","$").replace("\\)","$").replace("\\[","$").replace("\\]","$")

def extract_numbers(text):
	results = re.findall(r"[-+]?(?:\d*[.,]?\d+)", text)
	results = [float(r.replace(',','.')) for r in results]
	if len(results) == 0:
		results = [0]
	return results

def display_chat(messages,n_new=None):
	if n_new is not None:
		messages = messages[-n_new:]
	for message in messages:
		display(Markdown(f"----------"))
		display(Markdown(f"**{message['role']}:**"))
		display(Markdown(f"{message['content']}"))
