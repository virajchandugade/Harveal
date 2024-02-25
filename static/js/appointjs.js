function toggleAddressField() {
    var visitType = document.getElementById("visitType").value;
    var addressFields = document.querySelectorAll(".address-fields input");
    var locateMeButton = document.getElementById("locateMeButton");
    
    if (visitType === "physical") {
        addressFields.forEach(function(field) {
            field.removeAttribute("disabled");
        });
        locateMeButton.removeAttribute("disabled");
    } else {
        addressFields.forEach(function(field) {
            field.setAttribute("disabled", "disabled");
        });
        locateMeButton.setAttribute("disabled", "disabled");
    }
}

// Call toggleAddressField() when the page loads to handle pre-selected option
window.onload = function() {
    toggleAddressField();
};

function locateMe() {
    // You can write JavaScript code here to get user's location using IP address
    alert("Location will be located based on IP address.");
}

document.getElementById("appointmentForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    // Here you can write code to handle form submission, e.g., sending data to server
});

function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}
