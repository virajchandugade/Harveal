async function translateText() {
    try {
        const textInput = document.getElementById('textInput').innerText  ;

        const formData = new FormData();
        formData.append('text', textInput);

        const response = await fetch('/translate/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();

            const formattedText = result.translatedText.replace(/<br>/g, '\n');

            document.getElementById('translationResult').innerText = `Translated Text: ${formattedText}`;
            // document.getElementById('translationResult').innerText = `Translated Text: ${result.translatedText}`;
        } else {
            console.error('Failed to translate:', response.statusText);
        }
    } catch (error) {
        console.error('Error translating text:', error);
    }
}

async function translateTexthindi() {
    try {
        const textInput= document.getElementById('textInput').innerHTML  ;

        const formData = new FormData();
        formData.append('text_h', textInput);

        const response = await fetch('/translate_hindi/', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const resulth = await response.json();

            const formattedTexth = resulth.translatedText.replace(/<br>/g, '\n');

            document.getElementById('translationResult').innerText = `Translated Text: ${formattedTexth}`;
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
            // document.getElementById('audioContainer').innerHTML = '';
            document.getElementById('audioContainer').appendChild(audioElement);
        } else {
            console.error('Failed to read out loud:', response.statusText);
        }
    } catch (error) {
        console.error('Error reading out loud:', error);
    }
}

//------------------------------drag and drop------------------------------------------------------------------
// Add event listeners for drag and drop
function handleFileInput(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            document.getElementById('imgview').innerHTML = ''; // Clear previous image
            document.getElementById('imgview').appendChild(img); // Display new image
            img.style.width = 450+ 'px';
            img.style.height= 450+ 'px';
            document.getElementById('drdp').textContent='';
        };
        reader.readAsDataURL(file);
    }
}

function uploadImage() {
    document.getElementById('input-file').click(); // Trigger click event on file input
}

function allowDrop(event) {
    event.preventDefault();
}

function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            document.getElementById('imgview').innerHTML = ''; // Clear previous image
            document.getElementById('imgview').appendChild(img); // Display new image
            img.style.width = 450+ 'px';
            img.style.height= 450+ 'px';
            document.getElementById('drdp').textContent='';
        };
        reader.readAsDataURL(file);
    }
}


//prediction request---------------------------------------------------------------------------------------------------

async function detectDisease() {
    // Disable the button during detection
    document.getElementById('detect_disease').disabled = true;

    // Get the file input
    const fileInput = document.getElementById('input-file');
    const file = fileInput.files[0];

    const plantType = document.getElementById('plant_type').value;

    // Prepare the data to send to the FastAPI endpoint
    const formData = new FormData();
    formData.append('file', file);
    formData.append('plant_type', plantType);

    try {
        // Make an asynchronous request to the FastAPI endpoint
        const response = await fetch('/predmod/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            // Parse the JSON response
            const result = await response.json();

            // Display the result in the section
            document.getElementById('textInput').innerText  = result.result;
            console.log("success",result.result);
        } else {
            console.error('Failed to get prediction result');
        }
    } catch (error) {
        console.error('An error occurred during detection:', error);
    } finally {
        // Enable the button after detection is complete
        document.getElementById('detect_disease').disabled = false;
    }
}
