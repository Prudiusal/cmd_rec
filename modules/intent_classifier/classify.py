import os
import json
from dotenv import load_dotenv
from modules.utils.logger import logger
from .classification_models import ExtractIntention
from openai import AsyncOpenAI


load_dotenv()

client_classify = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

# async def classify_intent(text):
#     return {}

async def classify_intent(text: str) -> str:
    # try:
    response = await client_classify.with_options(max_retries=3).beta.chat.completions.parse(
        model="gpt-4o-mini", 
        response_format = ExtractIntention,
        temperature=0,
        # max_retries=4,
        messages = [{
            "role": "system",
            "content": "Analyze the user's text and extract the information.",
        },
        {
            "role": "user",
            "content": text
        }
        ]
    )
    res = json.loads(response.choices[0].message.to_dict()['content'])
    logger.debug(f'Res in classify is {res}')
    return res
#     except Exception as e:
#         logger.error(f"Error in transcribe_audio: {e}")
#         return {"error": str(e)}