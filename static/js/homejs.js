

var languages = ["Harveal, committed to plant health.", "हार्वील, पौधे स्वास्थ्य को समर्पित।", "हार्वील, वनस्पती स्वास्थ्यासाठी प्रतिबद्ध."];
var currentIndex = 0;

function rotateTextWithTransition() {
    document.getElementById("s1_h").style.opacity = 0; // Fade out text

    setTimeout(() => {
        document.getElementById("s1_h").textContent = languages[currentIndex]; // Update text content
        document.getElementById("s1_h").style.opacity = 1; // Fade in text
        currentIndex = (currentIndex + 1) % languages.length; // Move to the next language
        if (currentIndex === 0) { // If reached the end of one cycle
            clearInterval(intervalId); // Stop rotating text
        }
    }, 500); // Adjust timing to match transition duration
}

// Start rotating text on page load
window.onload = function () {
    rotateTextWithTransition();
    var intervalId = setInterval(rotateTextWithTransition, 5000); // Rotate text every 1.8 seconds
};

