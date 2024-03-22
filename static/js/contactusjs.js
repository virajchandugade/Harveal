async function writeus() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;

    if (name === '') {
        document.getElementById('n-error').textContent = "*Enter your name";
        document.getElementById('n-error').style.color = "red";
        return;
    } else {
        document.getElementById('n-error').textContent = "";
    }

    if (email === '') {
        document.getElementById('e-error').textContent = "*Enter your email";
        document.getElementById('e-error').style.color = "red";
        return;
    } else {
        document.getElementById('e-error').textContent = "";
    }

    if (message === '') {
        document.getElementById('m-error').textContent = "*Message cannot be left blank.";
        document.getElementById('m-error').style.color = "red";
        return;
    } else {
        document.getElementById('m-error').textContent = "";
    }

    var formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('message', message);

    try {
        const response = await fetch('/sub_contact/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            showsentbanner();
        } else {
            const err = await response.json();
            console.log(err);
            alert("An error occurred, please try again later!");
        }
    } catch (error) {
        console.log("Error :", error);
        alert("An error occurred, please try again later!");
    }
}


function showsentbanner() {
    var overlay = document.getElementById("overlay");
    var successBanner = document.getElementById("successBanner");
    var successMessage = document.getElementById("successMessage");

    var mess="Your query is submitted, we will get back to you soon.Happy Farming!";
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

