"""
translator.py
"""

import os
from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    """
    Translates from english to french
    """
    french_translation = language_translator.translate(
    text= englishtext,
    model_id= "en-fr").get_result()

    french_text = french_translation.get("translations")[0].get("translation")

    return french_text

def french_to_english(frenchtext):
    """
    Translates from french to english
    """
    english_translation = language_translator.translate(
    text= frenchtext,
    model_id= "fr-en").get_result()

    english_text = english_translation.get("translations")[0].get("translation")

    return english_text
