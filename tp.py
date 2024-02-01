# import googletrans
# from googletrans import Translator


# translator = Translator()
# result = translator.translate('Tomato mosaic virus (ToMV) is a plant pathogenic virus. It is found worldwide and affects tomatoes and many other plants.', src='en', dest='mr')
# print(result)

from translate import Translator
translator= Translator(to_lang="mr")
translation = translator.translate("Tomato mosaic virus (ToMV) is a plant pathogenic virus. It is found worldwide and affects tomatoes and many other plants.")
print("heinnn")
print(translation)
