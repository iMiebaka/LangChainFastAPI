from settings import SETTINGS
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.messages import HumanMessage, AIMessage
import openai

def bot_response():
    try:
        model = ChatOpenAI(model="gpt-3.5-turbo")
        res = model.invoke([HumanMessage(content="Hi! I'm Bob")])
        return res.content
    except openai.RateLimitError:
        raise Exception("Rate limit exceeded. Please try again later.")
    except Exception:
        raise Exception("I'm sorry, I'm experiencing some technical difficulties. Please try again later.")