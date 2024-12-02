# import asyncio
# import json
# import pytest
# # from websockets import connect
# from unittest.mock import patch
# from unittest.mock import AsyncMock
# from modules.web_api.websocket_handler import handle_connection, start_websocket_server


# @pytest.fixture
# def mock_env(monkeypatch):
#     # Mock the HOST and PORT environment variables
#     monkeypatch.setenv("HOST", "localhost")
#     monkeypatch.setenv("PORT", "8765")


# @pytest.mark.asyncio
# async def test_handle_connection_valid_message():
#     # Mock the websocket object
#     mock_websocket = AsyncMock()
    
#     # Simulate a valid incoming message
#     input_message = json.dumps({"userId": "123", "audio": "some_audio_data", "text": "hello"})
#     mock_websocket.__aiter__.return_value = [input_message]  # Mock the async iteration over websocket
    
#     # Call the handler
#     await handle_connection(mock_websocket)
    
#     # Verify the response was sent
#     expected_response = json.dumps({"text": "HELLO"})
#     mock_websocket.send.assert_awaited_with(expected_response)


# @pytest.mark.asyncio
# async def test_handle_connection_invalid_message():
#     # Mock the websocket object
#     mock_websocket = AsyncMock()
    
#     # Simulate an invalid incoming message
#     invalid_message = "not a json"
#     mock_websocket.__aiter__.return_value = [invalid_message]  # Mock async iteration over websocket
    
#     # Call the handler
#     await handle_connection(mock_websocket)
    
#     # Verify the error response was sent
#     expected_error = {"userId": None, "error": "Expecting value: line 1 column 1 (char 0)"}
#     mock_websocket.send.assert_awaited_with(json.dumps(expected_error))


# @pytest.mark.asyncio
# async def test_handle_connection_missing_text_audio_key():
#     # Mock the websocket object
#     mock_websocket = AsyncMock()
    
#     # Simulate a message missing the 'text' and 'audio' key
#     input_message = json.dumps({"userId": "123"})
#     mock_websocket.__aiter__.return_value = [input_message]
    
#     # Call the handler
#     await handle_connection(mock_websocket)
    
#     # Verify the response was sent
#     expected_response = json.dumps({"error": "no data provided"})
#     mock_websocket.send.assert_awaited_with(expected_response)