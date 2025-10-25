import langchain
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
model = init_chat_model("groq:llama-3.1-8b-instant")
messages = [
    SystemMessage("You are a helpful AI assitant"),
    HumanMessage("what are the top 2 benifits of using langchain")
]
response=model.invoke(messages)
print(response.content)