// document.addEventListener('DOMContentLoaded', function () {
//     document.getElementById('login-btn').addEventListener('click', submit_apt);
// });

// async function submit_apt(event) {
//     event.preventDefault(); // Prevent default form submission behavior
    
//     var adminId = document.getElementById('admin-id').value;
//     var password = document.getElementById('password').value;

//     // Basic validation for admin ID and password
//     if (adminId === "") {
//         document.getElementById('error').textContent = '* Please enter your respective ID';
//         document.getElementById('error').style.color = 'red';
//         return;
//     } else {
//         document.getElementById('error').textContent = '';
//     }

//     if (password === "") {
//         document.getElementById('error-pass').textContent = '* Please enter your password';
//         document.getElementById('error-pass').style.color = 'red';
//         return;
//     } else {
//         document.getElementById('error-pass').textContent = '';
//     }

//     try {
//         // Create FormData object and append admin ID and password
//         var formData = new FormData();
//         formData.append('admin_id', adminId);
//         formData.append('password', password);

//         // Make a POST request to the FastAPI endpoint
//         const response = await fetch('/admin-login/', {
//             method: 'POST',
//             body: formData
//         });

//         if (response.ok) {
//             // Handle successful login
//             alert("Login successful!"); // or any other action
//         } else {
//             // Handle login failure
//             console.error('Login failed');
//             alert("Login failed. Please check your credentials."); // or any other action
//         }
//     } catch (error) {
//         console.error('Error during login:', error);
//         alert('An error occurred during login. Please try again later.');
//     }
// }
