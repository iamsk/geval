import os
from dify_client import ChatClient


class Base(object):
    def __init__(self, api_key):
        self.name = self.api_key = api_key

    def chat(self, query):
        chat_client = ChatClient(self.api_key)
        chat_response = chat_client.create_chat_message(inputs={}, query=query, user="geval",
                                                        response_mode="blocking")
        chat_response.raise_for_status()
        content = chat_response.json()['answer']
        return content


dify = Base(os.getenv('DIFY_APP_KEY'))
