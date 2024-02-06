
from translate import Translator

def translate_text(text, target_language='mr'):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text

# Example usage
english_text = "Hello, how are you?"
translated_text = translate_text(english_text, target_language='hi')
print(translated_text)





# import googletrans
# from googletrans import Translator

# translator = Translator()
# result = translator.translate('Tomato mosaic virus (ToMV) is a plant pathogenic virus. It is found worldwide and affects tomatoes and many other plants.', src='en', dest='hi')
# print(result)


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi


# uri = "mongodb+srv://harveal:harveal2024@cluster0.25sb0oo.mongodb.net/?retryWrites=true&w=majority"

# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client["harveal"]
# collection = db["disease"]


# dataENT = {
#     "d_id": "ToMV",
#     "d_name": "Tomato Mosaic Virus",
#     "d_desc": """Introduction:
#     Tomato Mosaic Virus (ToMV) is a common plant virus affecting tomatoes and various other plants worldwide.

#     Symptoms:
#     - Mottled leaves with yellow and dark green areas, giving a blister-like appearance.
#     - Fern-like leaves with pointed tips; younger leaves may be twisted.
#     - Distorted fruit with yellow blotches and necrotic spots.
#     - Internal browning of the fruit wall.
#     - Reduced fruit set and potential plant dwarfing.

#     Means of Infection:
#     - Spread through infected seeds and contaminated tools.
#     - Easily transmitted by hands and clothing during routine activities.

#     Disease Information:
#     - Type: Virus
#     - Classification:
#         - Realm: Riboviria
#         - Kingdom: Orthornavirae
#         - Phylum: Kitrinoviricota
#         - Class: Alsuviricetes
#         - Order: Martellivirales
#         - Family: Virgaviridae
#         - Genus: Tobamovirus
#         - Species: Tomato mosaic virus

#     Cure:
#     - No direct cure for infected plants; focus on prevention.

#     Preventive Measures:
#     1. Opt for virus-resistant tomato cultivars.
#     2. Promptly remove and destroy infected plants to prevent the virus spread.
#     3. Purchase transplants from reliable retailers.
#     4. Inspect transplants for any symptoms before buying.
#     5. Frequent disinfection of tools, especially between plants.
#     6. No effective chemical solutions; control aphids and thrips to prevent virus spread.

#     Key Takeaway:
#     Early detection and preventive measures are crucial to manage Tomato Mosaic Virus. Choose resistant cultivars, inspect transplants, and maintain good hygiene to safeguard your tomato plants.
#     """
# }

# # collection.insert_one(dataENT)
    
# a=collection.find_one({"d_id":"ToMV"})
# print(a)



