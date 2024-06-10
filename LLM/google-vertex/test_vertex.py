import getpass
import os

from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage, SystemMessage

os.environ["GOOGLE_API_KEY"] = getpass.getpass()
model = ChatVertexAI(model="gemini-pro")

messages = [
    SystemMessage(content="Translate the following from English into German"),
    HumanMessage(content="hi, how can we help you?"),
]

model.invoke(messages)
