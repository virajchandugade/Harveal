function toggleAddressField() {
    var visitType = document.getElementById("visitType").value;
    var addressFields = document.querySelectorAll(".address-fields input, .address-fields select");
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

//----------------------------------------------------appointment_submission------------------------------------------------

async function submitForm() {
    var hid = document.getElementById("hid").value;
    var fullname = document.getElementById("fullname").value;
    var dob = document.getElementById("dob").value;
    var contact = document.getElementById("contact").value;
    var plant = document.getElementById("plant").value;
    var description = document.getElementById("description").value;
    var visitType = document.getElementById("visitType").value;
    var houseNumber = document.getElementById("houseNumber").value;
    var street = document.getElementById("street").value;
    var city = document.getElementById("city").value;
    var state = document.getElementById("state").value;
    var pincode = document.getElementById("pincode").value;

    var formData = new FormData();
    formData.append("hid", hid);
    formData.append("fullname", fullname);
    formData.append("dob", dob);
    formData.append("contact", contact);
    formData.append("plant", plant);
    formData.append("description", description);
    formData.append("visitType", visitType);
    formData.append("houseNumber", houseNumber);
    formData.append("street", street);
    formData.append("city", city);
    formData.append("state", state);
    formData.append("pincode", pincode);

    try {
        const response = await fetch("/submit_appn/", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            
            alert("Form submitted successfully!");
            showSuccessBanner();
            
        } else {
            const errorData = await response.json();
            console.error(errorData);
            alert("Error submitting form. Please check your inputs and try again.");
        }
    } catch (error) {
        console.error("An unexpected error occurred:", error);
        alert("An unexpected error occurred. Please try again.");
    }
}
//----------------------------------------------------------successmessage--------------------------------------------
function showSuccessBanner() {
    var overlay = document.getElementById("overlay");
    var successBanner = document.getElementById("successBanner");
    var successMessage = document.getElementById("successMessage");

    var mess="your appointment is escalated, the email is been sent to your registered  email id";
    // Set the success message text
    successMessage.textContent =mess ;
    // Set the success message text

    // Show the overlay and success banner
    overlay.style.display = "block";
    successBanner.style.display = "block";

    // Auto-dismiss after 10 seconds
    setTimeout(dismissBanner, 10000);
}

function dismissBanner() {
    var overlay = document.getElementById("overlay");
    var successBanner = document.getElementById("successBanner");

    // Hide the overlay and success banner
    overlay.style.display = "none";
    successBanner.style.display = "none";
}