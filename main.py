import os
import asyncio
import traceback
from modules.web_api.websocket_handler import start_websocket_server
from modules.utils.logger import logger
from dotenv import load_dotenv
from modules.utils.check_envs import check_env_vars

load_dotenv()
check_env_vars(['PYTHONASYNCIODEBUG'])
debug_flag = bool(int(os.getenv('PYTHONASYNCIODEBUG')))

async def main():
    logger.info("Starting the server...")
    try:
        await start_websocket_server()
        # TODO Move here
        # async with websockets.serve(handle_connection, HOST, PORT):
        #     await asyncio.Future()
    except Exception as e:
        logger.error(f"Server crashed: {e}")
        logger.error(f"Exception type: {type(e).__name__}")
        logger.error(f"Exception message: {str(e)}")
        logger.error(f"Stack trace: {traceback.format_exc()}")


if __name__ == "__main__":
    logger.info(f'{debug_flag=}')
    asyncio.run(main(), debug=debug_flag)
    