# Chatbot using Langchain and OpenAI
This is a simple chatbot implementation using Langchain and OpenAI's GPT-3.5-turbo model.

Usage
To use this chatbot, simply call the bot_response() function and pass in a human message as a string. The function will return the chatbot's response as a string.

The code consists of a single function bot_response() that:


Imports the necessary modules from Langchain and OpenAI.
Creates a ChatOpenAI model instance with the GPT-3.5-turbo model.
Invokes the model with a human message ("Hi! I'm Bob") and returns the response.
Catches any RateLimitError exceptions raised by OpenAI and prints an error message.

```py
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
        print("Rate limit exceeded. Please try again later.")
        return None
```


Example
Edit
```py
print(bot_response())
```
This will output the chatbot's response to the message "Hi! I'm Bob".

Note
This implementation assumes you have the necessary credentials set up for OpenAI and Langchain. You may need to modify the code to fit your specific use case.