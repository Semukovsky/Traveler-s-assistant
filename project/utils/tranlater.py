from deep_translator import GoogleTranslator


def translate(from_language, to_language, text):
    translator = GoogleTranslator(source=from_language, target=to_language)
    return translator.translate(text)
