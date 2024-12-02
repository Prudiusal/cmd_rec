import base64
import asyncio
import json
import websockets
import pytest
from modules.transcription.process_transcription import transcribe_audio


def encode_audio_file(file_path):
    with open(file_path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode("utf-8")


@pytest.mark.asyncio
async def test_websocket_request():
    # Encode the .ogg file
    audio_file_path = "data/sample_rec.ogg"  # Path to your .ogg file
    encoded_audio = encode_audio_file(audio_file_path)

    # Prepare the WebSocket request payload
    message = json.dumps({
        "userId": "test_user",
        "audio": encoded_audio
    })

    # Send the request to the WebSocket server
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)

        # Receive and print the response
        response = await websocket.recv()
        print("Server Response:", response)

