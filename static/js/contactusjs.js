async function writeus(){
    var name=document.getElementById("name").value;
    var email=document.getElementById("email").value;
    var message=document.getElementById("message").value;

    if (name===''){
        var er=document.getElementById('n-error');
        er.textContent="enter your name";
        er.style.color="red";
        document.getElementById("name").style.border= "2px solid red";
        return

    }
    else {
        var er=document.getElementById('n-error');
        er.textContent="";
        er.style.color="";
        document.getElementById("name").style.border= "";
        
    }

    if (email===''){
        var er=document.getElementById('e-error');
        er.textContent="enter your email";
        er.style.color="red";
        document.getElementById("email").style.border= "2px solid red";
        return

    }
    else {
        var er=document.getElementById('e-error');
        er.textContent="";
        er.style.color="";
        document.getElementById("email").style.border= "";
        
    }


    if (message===''){
        var er=document.getElementById('m-error');
        er.textContent="message cannot be left blank.";
        er.style.color="red";
        document.getElementById("email").style.border= "2px solid red";
        return

    }
    else {
        var er=document.getElementById('e-error');
        er.textContent="";
        er.style.color="";
        document.getElementById("email").style.border= "";
        
    }

    var formData=new FormData()
    formData.append('name', name)
    formData.append('email', email)
    formData.append('message', message)

    try{
        const response= await fetch('/contactus/',{
            method:'POST',  
            body:formData
        });
        
        if (response.ok) { 
            showsentbanner();
    }
    else{
        const err=await response.json();
        console.log(err);
        alert("error occured, try after sometime!");
    }
    }
    catch(error){
        console.log("Error :",error);
        alert("error occured, try after sometime!");

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

