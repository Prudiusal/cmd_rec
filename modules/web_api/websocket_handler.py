import asyncio
import websockets
import traceback
import json
import os

from dotenv import load_dotenv

# from modules.transcription.process_transcription import transcribe_audio
# from modules.intent_classifier.classify import classify_intent
# from modules.pricing.token_calculation import calculate_price_request
# from modules.database.db_operations import log_request, log_error
from modules.request_manager.manager import manage_request
from modules.utils.logger import logger
from modules.utils.check_envs import check_env_vars


load_dotenv()
check_env_vars(["WEBSOCKET_HOST", "WEBSOCKET_PORT"])
HOST = os.getenv("WEBSOCKET_HOST", "0.0.0.01")
PORT = int(os.getenv("WEBSOCKET_PORT", 8765))


async def handle_connection(websocket):
    async for message in websocket:
        user_id = None
        try:
            data = json.loads(message)

            user_id = data.get("userId")
            audio = data.get("audio")
            data['audio'] = 'DELETED_BYTES'
            text = data.get("text")

            if not (text or audio):
                response = {"error": "no data provided"}
                await websocket.send(json.dumps(response))
                continue

            response = await manage_request(user_id, audio, text)
            if not isinstance(response, dict):
                logger.error(str(response))
                response = {"error": "wrong data type from manage_request"}
                await websocket.send(json.dumps(response))
                continue

            logger.debug(f"response: {response}")
            await websocket.send(json.dumps(response))
        except Exception as e:
            # Log detailed error info
            if data.get('audio'):
                data['audio'] = 'DELETED_BYTES'
            logger.error(f"Error occurred while processing message: {data}")
            logger.error(f"Exception type: {type(e).__name__}")
            logger.error(f"Exception message: {str(e)}")
            logger.error(f"Stack trace: {traceback.format_exc()}")

            # Send a detailed error response
            error_response = {
                "userId": user_id,
                "error": str(e),
                "error_type": type(e).__name__,
                "message": message,  # Add the incoming message to the response if appropriate
            }
            await websocket.send(json.dumps(error_response))
        # except Exception as e:
        #     await websocket.send(json.dumps({"userId": user_id, "error": str(e)}))
        #     # log_error(f"Error handling request: {e}")
            #  await websocket.send(json.dumps({"error": str(e)}))
        

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def start_websocket_server():
    logger.info(f"WebSocket server running on {HOST}:{PORT}")
    async with websockets.serve(handle_connection, HOST, PORT):
        await asyncio.Future()  # Keep the server running
    # async with websockets.serve(echo, host, port):
        # await asyncio.Future()  # Keep the server running
