""" Translates English and French """
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    """ Translates English text to French """
    response = translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    return response['translations'][0]['translation']

def french_to_english(french_text):
    #write the code here
    """ Translates French text to English """
    response = translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    return response['translations'][0]['translation']
