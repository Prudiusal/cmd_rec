import os
from dotenv import load_dotenv
from modules.utils.logger import logger
from openai import AsyncOpenAI
import base64
from io import BytesIO
# import aiofiles
# import asyncio
# import base64
# import tempfile


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client_transcribe = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)


# async def async_remove(file_path):
#     """Asynchronously remove a file."""
#     loop = asyncio.get_event_loop()
#     await loop.run_in_executor(None, os.remove, file_path)


async def transcribe_audio(base64_audio) -> dict:
    try:
        if not base64_audio:
            raise ValueError("No audio data provided")
        # logger.debug(f'{base64_audio=}')
        audio_bytes = base64.b64decode(base64_audio)
    
        # audio_file = BytesIO(audio_bytes)
        
        response = await client_transcribe.audio.transcriptions.create(
                model="whisper-1",
                # file=base64_audio, 
                file = ('temp.ogg', audio_bytes, 'audio/ogg'),
                # file=audio_bytes, 
                # file=audio_file,
                response_format="text",
                language='en'  
            )
        
        transcription = response
        return {"transcription": transcription}

    except Exception as e:
        logger.error(f"Error in transcribe_audio: {e}")
        return {"error": str(e)}


# async def transcribe_audio4(base64_audio) -> dict:
#     try:
#         # Validate and decode Base64 audio
#         if not base64_audio:
#             raise ValueError("No audio data provided")
        
#         try:
#             decoded_audio = base64.b64decode(base64_audio)
#         except Exception as decode_error:
#             raise ValueError("Invalid Base64 audio data") from decode_error

#         # Save decoded audio to a temporary file asynchronously
#         temp_file = tempfile.NamedTemporaryFile(suffix=".ogg", delete=False)
#         temp_audio_path = temp_file.name
#         temp_file.close()  # Close the temp file to avoid conflicts in async mode
        
#         async with aiofiles.open(temp_audio_path, "wb") as temp_audio:
#             await temp_audio.write(decoded_audio)
#         # with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as temp_audio:
#         #     temp_audio.write(decoded_audio)
#         #     temp_audio_path = temp_audio.name
#         logger.debug(f'{type(temp_audio_path)=}')
#         logger.debug(f'{temp_audio_path=}')


#         # try:
#             # Open the temp file asynchronously for reading
#         with open(temp_audio_path, "rb") as audio_file:
#         # async with aiofiles.open(temp_audio_path, "rb") as audio_file:
#             response = await client_transcribe.audio.transcriptions.create(
#                 model="whisper-1",
#                 file=audio_file,  # Ensure the client supports async file handling
#                 response_format="text",
#                 language='en'  # Options: text, json, or srt
#             )
#         transcription = response

#         # finally:
#             # Clean up the temporary file asynchronously
#         if os.path.exists(temp_audio_path):
#             await async_remove(temp_audio_path)

#         return {"transcription": transcription}

#     except Exception as e:
#         logger.error(f"Error in transcribe_audio3: {e}")
#         return {"error": str(e)}


# async def transcribe_audio2(base64_audio):
#     try:
#         # Decode the Base64 audio and save to a temporary file
#         decoded_audio = base64.b64decode(base64_audio)
#         with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as temp_audio:
#             temp_audio.write(decoded_audio)
#             temp_audio_path = temp_audio.name

#         # Initialize LangChain's WhisperParser
#         parser = FasterWhisperParser()

#         # Transcribe the audio file
#         transcription_result = parser.parse_file(temp_audio_path)

#         # Extract text from the transcription result
#         transcription = transcription_result.text

#         return transcription
#     except Exception as e:
#         logger.error(f"Error in process_audio: {e}")
#         return {"error": str(e)}


# async def transcribe_audio(audio_data):
#     try:
#         response = openai.Audio.transcribe("whisper-1", audio_data)
#         transcription = response.get("text", "")
#         logger.info("Audio transcribed successfully")
#         return transcription
#     except Exception as e:
#         logger.error(f"Audio transcription failed: {e}")
#         # raise



# async def transcribe_audio1(base64_audio):
    
#     try:
#         # Decode the Base64 audio and save to a temporary file
#         decoded_audio = base64.b64decode(base64_audio)
#         with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as temp_audio:
#             temp_audio.write(decoded_audio)
#             temp_audio_path = temp_audio.name

#         # Send the file to OpenAI Whisper for transcription
#         with open(temp_audio_path, "rb") as audio_file:
#             transcription_result = openai.Audio.transcribe("whisper-1", audio_file)
#         logger.info(f"Returning text {transcription_result.get('text')}")

#         return transcription_result.get("text")
#     except Exception as e:
#         logger.error(f"Error in process_audio: {e}")
#         return {"error": str(e)}
