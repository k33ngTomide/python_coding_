
from translate import Translator

translator = Translator(to_lang='ja', from_lang='en')

text = "Testosterone"
translated_text = translator.translate(text)
print(translated_text)

