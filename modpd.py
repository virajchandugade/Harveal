import tensorflow as tf
pip install gtts

from gtts import gTTS
import os

def text_to_speech(text, lang='mr'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)

    # Save the generated speech as an audio file
    tts.save("output.mp3")

    # Play the generated audio file
    os.system("start output.mp3")

if __name__ == "__main__":
    # Input the Hindi text you want to convert to speech
    hindi_text = "टोमॅटो मोज़ेक विषाणू हा वनस्पतीजन्य रोगजनक विषाणू आहे. हे जगभरात आढळते आणि टोमॅटो आणि इतर अनेक वनस्पतींना प्रभावित करते"
    # "हमें फुटबॉल पसंद है"
    # Call the function to convert text to speech
    text_to_speech(hindi_text)
