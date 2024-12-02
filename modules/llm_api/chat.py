# import os
# from dotenv import load_dotenv
# # from langchain.chat_models import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# # from langchain.schema import HumanMessage
# from langchain_openai import ChatOpenAI
# # from langchain_community.chat_models import ChatOpenAI
# from langchain_core.messages import HumanMessage, SystemMessage


# from modules.utils.logger import logger

# # Load the API key from the .env file
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# PROMPT_TEMPLATE = """
# You are Liza, the wise master of music. Your role is to discuss music topics and guide users on how to create nice sounds and explore musical styles.

# You answer shortly but with a touch of mystery and magic. You avoid politics, news, harmful topics, or anything negative.

# Stick strictly to music-related discussions. Here is the user input:

# {human_input}
# """
# chat_model = ChatOpenAI(model="gpt-4o-mini")
#     # chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4", temperature=0.7)


# # Function to initialize the LangChain chatbot
# async def get_chatbot_response(user_input: str, prompt_template: str = PROMPT_TEMPLATE):
#     """
#     Generate a response from the OpenAI chatbot.
#     Args:
#         user_input (str): The text input from the user.
#     Returns:
#         str: The chatbot's response.
#     """
#     logger.info(f"Recieved: {user_input}")
#     # Initialize the chat model with the OpenAI API key
#     # chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4", temperature=0.7)
    
#     # Use a template to structure the prompt
#     # prompt = ChatPromptTemplate.from_template(prompt_template)
    
#     # Prepare the messages
#     # messages = prompt.format_messages(human_input=user_input)
    
#     # Get the response asynchronously
#     # response = await chat.agenerate(messages=messages)
#     logger.info(f"Anser: {response.generations[0].message.content}")
    
#     # Return the first response from the assistant
#     # return response.generations[0].message.content
