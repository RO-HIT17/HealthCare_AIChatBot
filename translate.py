from googletrans import Translator

def translate_tamil_to_english(tamil_text):
    translator = Translator()
    
    translated = translator.translate(tamil_text, src='ta', dest='en')
    
    return translated.text

if __name__ == "__main__":
    tamil_text = "எனக்கு காய்ச்சலும் உள்ளது"
    
    english_translation = translate_tamil_to_english(tamil_text)
    
    print("Tamil Text:", tamil_text)
    print("English Translation:", english_translation)
