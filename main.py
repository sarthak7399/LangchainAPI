from langchain.schema import AIMessage,HumanMessage,SystemMessage
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3)

messages = [
    SystemMessage(content="You are a funny and helpful assistant."),
    HumanMessage(content="Explain to me quantum physics."),
]
response=chat(messages)

print(response.content,end='\n')