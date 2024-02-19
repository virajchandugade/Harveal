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

async function translateTexthindi() {
    try {
        const textInput= document.getElementById('textInput').value;

        const formData = new FormData();
        formData.append('text_h', textInput);

        const response = await fetch('/translate_hindi/', {
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

//------------------------------drag and drop------------------------------------------------------------------
const droparea=document.getElementById('drop-area');
const inputfile=document.getElementById('input-file');
const imgview=document.getElementById('imgview');

inputfile.addEventListener("change",uploadimage)

function uploadimage(){
    
    let imglink=URL.createObjectURL(inputfile.files[0]);
    imgview.style.backgroundImage=`url( ${imglink})`; 
    imgview.textContent="";
}

droparea.addEventListener( "dragover", function( event ){
    event.preventDefault();
});

droparea.addEventListener( "drop", function( event ){
    event.preventDefault();
    inputfile.files=event.dataTransfer.files;
    uploadimage();
});


//prediction request---------------------------------------------------------------------------------------------------

  async function detectDisease() {
    // Disable the button during detection
    document.getElementById('detect_disease').disabled = true;

    // Disable the textarea during detection
    document.getElementById('textInput').disabled = true;

    // Get the file input
    const fileInput = document.getElementById('input-file');
    const file = fileInput.files[0];

    // Prepare the data to send to the FastAPI endpoint
    const formData = new FormData();
    formData.append('file', file);

    try {
        // Make an asynchronous request to the FastAPI endpoint
        const response = await fetch('/predmod/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            // Parse the JSON response
            const result = await response.json();

            // Display the result in the textarea
            document.getElementById('textInput').value = result.result;
        } else {
            console.error('Failed to get prediction result');
        }
    } catch (error) {
        console.error('An error occurred during detection:', error);
    } finally {
        // Enable the button and textarea after detection is complete
        document.getElementById('detect_disease').disabled = false;
        document.getElementById('textInput').disabled = false;
    }
}