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

function handleDragOver(event) {
    event.preventDefault();
    document.getElementById('drop-area').classList.add('highlight');
  }

  function handleDragLeave(event) {
    event.preventDefault();
    document.getElementById('drop-area').classList.remove('highlight');
  }

  function handleDrop(event) {
    event.preventDefault();
    document.getElementById('drop-area').classList.remove('highlight');

    const files = event.dataTransfer.files;

    if (files.length > 0) {
      const imageFile = files[0];
      displayImage(imageFile);
    }
  }

  function handleFiles(files) {
    if (files.length > 0) {
      const imageFile = files[0];
      displayImage(imageFile);
    }
  }

  function displayImage(file) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const imgElement = document.getElementById('preview-img');
      imgElement.src = e.target.result;
      imgElement.alt = file.name;
      imgElement.style.display = 'block';
      
      document.getElementById('drop-area').innerHTML = ''; // Clear previous content
      document.getElementById('drop-area').appendChild(imgElement);
    };

    reader.readAsDataURL(file);
  }

  function openFileExplorer() {
    document.getElementById('file-input').click();
  }