import requests

host = "http://127.0.0.1:8000/api/chatbot?infos="

def skype_chat(msg):
    respose = requests.get(host+msg)
    get_rest = respose.text
    return get_rest
