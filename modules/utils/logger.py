import logging

logging.basicConfig(
    # level=logging.INFO,
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(filename)s: %(message)s", 
    handlers=[logging.StreamHandler(), logging.FileHandler("app.log")],
)
logger = logging.getLogger(__name__)

logging.getLogger("asyncio").setLevel(logging.DEBUG)