# import the name of the model from the dotenv and use it for the calculation

# https://github.com/openai/tiktoken

def calculate_price_request(request: str):
    return int(bool(request))

 
def calculate_price_response(response: str):
    return int(bool(response))