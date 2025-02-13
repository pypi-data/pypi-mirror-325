from deep_translator import GoogleTranslator
from langdetect import detect

class AutoTranslate:
    def __init__(self, selected_lang: str = "en"):
        self.selected_lang = selected_lang.lower()
    
    def translate(self, text: str):
        try:
            detected_lang = detect(text)
            if detected_lang == self.selected_lang:
                return text  # No need to translate
            return GoogleTranslator(source='auto', target=self.selected_lang).translate(text)
        except Exception as e:
            return f"Translation error: {e}"
