async function translateText() {
    try {
        const textInput = document.getElementById('textInput').value;

        const formData = new FormData();
        formData.append('text', textInput);

        const response = await fetch('/translate/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('translationResult').innerText = `Translated Text: ${result.translatedText}`;
        } else {
            console.error('Failed to translate:', response.statusText);
        }
    } catch (error) {
        console.error('Error translating text:', error);
    }
}

async function readOutLoud() {
    try {
        const readOutLoudInput = document.getElementById('translationResult').innerText;

        const formData = new FormData();
        formData.append('text', readOutLoudInput);

        const response = await fetch('/read_out_loud/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const audioUrl = await response.json();
            // Create an audio element
            const audioElement = document.createElement('audio');
            audioElement.src = audioUrl.audio_url;
            audioElement.controls = true;

            // Append the audio element to the document
            document.getElementById('audioContainer').innerHTML = '';
            document.getElementById('audioContainer').appendChild(audioElement);
        } else {
            console.error('Failed to read out loud:', response.statusText);
        }
    } catch (error) {
        console.error('Error reading out loud:', error);
    }
}