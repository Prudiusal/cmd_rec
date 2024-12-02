from modules.intent_classifier.classify import classify_intent
from modules.transcription.process_transcription import transcribe_audio   
from modules.utils.logger import logger
# from modules.llm_api.chat import get_chatbot_response
# from modules.llm_api import chat_with_user, generate_midi, modify_midi, generate_sound
# from modules.utils.logger import logger 


async def manage_request(user_id, audio, text) -> dict:
    # Classify the intent if not presented in the requst
    logger.debug(f"Recieved text: {text}")
    if audio:
        transcription_res = await transcribe_audio(audio)
        if transcription_res.get('error'):
            return transcription_res
        else:
            text = transcription_res['transcription']
            logger.info(f'Transcripted: {text}')

    classification_response = await classify_intent(text)
    classification_response['userId'] = user_id
    intent = classification_response['intention']

    if intent == "voice_command":
        return classification_response
    else:
        return {"error": f"Unsupported intent: {intent}"}
