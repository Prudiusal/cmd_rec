import requests
import pytest
import os
from dotenv import load_dotenv


# Load OpenAI API key from environment variable or configuration
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def test_openai_connection():
    url = "https://api.openai.com/v1/models"
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Connection failed with status code {response.status_code}. Response: {response.text}"


def test_invalid_api_key():
    url = "https://api.openai.com/v1/models"
    # Provide an invalid API key for the test
    invalid_api_key = "INVALID_API_KEY"
    headers = {
        "Authorization": f"Bearer {invalid_api_key}"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 401, f"Expected 401 for invalid key, got {response.status_code}. Response: {response.text}"
    assert "Incorrect API key provided" in response.text, f"Unexpected error message: {response.text}"


def test_valid_api_key():
    url = "https://api.openai.com/v1/models"
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200, f"Invalid API key. Response: {response.text}"
    
    # Optional: Check if the response includes a list of models (i.e., valid response)
    models = response.json().get('data', [])
    assert len(models) > 0, "No models returned, the API key might be invalid."


def test_empty_api_key():
    url = "https://api.openai.com/v1/models"
    
    headers = {
        "Authorization": "Bearer "
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 401, f"Expected 401 for missing API key, got {response.status_code}. Response: {response.text}"
    assert "Incorrect API key provided" in response.text, f"Unexpected error message: {response.text}"
