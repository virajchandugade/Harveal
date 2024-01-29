let register_btn = document.querySelector(".Register-btn");
let login_btn = document.querySelector(".Login-btn");
let form = document.querySelector(".Form-box");
register_btn.addEventListener("click", () => {
  form.classList.add("change-form");
});
login_btn.addEventListener("click", () => {
  form.classList.remove("change-form");
});

function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}

function enableGetOtp() {
  const phone = document.getElementById('phone').value;
  const email = document.getElementById('email').value;
  const getOtpBtn = document.getElementById('getOtpBtn');

  if (phone.trim() !== '' && email.trim() !== '') {
      getOtpBtn.removeAttribute('disabled');
  } else {
      getOtpBtn.setAttribute('disabled', 'true');
  }

}

// JavaScript function to enable Submit button when OTP is entered
function enableSubmit() {
  const otp = document.getElementById('otp').value;
  const submitBtn = document.getElementById('submitBtn');

  if (otp.trim() !== '') {
      submitBtn.removeAttribute('disabled');
  } else {
      submitBtn.setAttribute('disabled', 'true');
  }
}


// JavaScript function to submit the form (replace with your actual form submission logic)

// mode: 'cors',

async function sendOtp() {
  try {
    // Get the email value from the input field
    const email = document.getElementById('email').value;

    // Make a fetch request to the /sendotp/ endpoint
    const response = await fetch('/sendotp/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email }),
    });

    // Check if the request was successful
    if (response.ok) {
      // If successful, enable the OTP input field
      // Enable the Submit button
      
      alert('OTP Sent!');
      document.getElementById('otp').removeAttribute('disabled');
      enableSubmit();
    } else {
      // If not successful, handle the error (e.g., display an error message)
      console.error('Failed to send OTP:', response.statusText);
    }
  } catch (error) {
    console.error('Error sending OTP:', error);
  }
}

//for login form submit
function enableLogSubmit() {
  const logotp = document.getElementById('logOTP').value;
  const logsubmitBtn = document.getElementById('submitLog-btn');

  if (logotp.trim() !== '') {
      logsubmitBtn.removeAttribute('disabled');
  } else {
      logsubmitBtn.setAttribute('disabled', 'true');
  }
}
//for login form get otp button
function enableLogotp(){
  const user_id=document.getElementById('logID').value;
  const loggetOtpBtn = document.getElementById('getlogotp-btn');

  if (user_id.trim() !== '') {
      loggetOtpBtn.removeAttribute('disabled');
  } else {
      loggetOtpBtn.setAttribute('disabled', 'true');
  }
}

//for login form otp sending logic
async function sendLogOtp() {
  try {
    // Get the email value from the input field
    const uid = document.getElementById('logID').value;

    // Make a fetch request to the /sendotp/ endpoint
    const logresponse = await fetch('/send_log_otp/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ uid }),
    });

    // Check if the request was successful
    if (logresponse.ok) {
      // If successful, enable the OTP input field
      // Enable the Submit button
      
      alert('OTP Sent!');
      document.getElementById('logOTP').removeAttribute('disabled');
      enableLogSubmit();
    } else {
      // If not successful, handle the error (e.g., display an error message)
      console.error('Failed to send OTP:', logresponse.statusText);

    }
  } catch (error) {
    console.error('Error sending OTP:', error);
  }
}


