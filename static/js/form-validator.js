function validate()
{
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const mobile = document.getElementById('mobile').value;
    let error  = false;


    //NAME
    if(name === "")
    {
        //console.log("Name is required");
        document.getElementById("name_error").innerHTML = "Name is required!";
        error = true;
    }
    else{
        document.getElementById("name_error").innerHTML = "";
    }



    //MOBILE
    if(mobile === "")
    {
        document.getElementById("mobile_error").innerHTML = "Mobile number is required";
        error = true;
    }
    else if(mobile.length != 11 || isNaN(mobile)){
        document.getElementById("mobile_error").innerHTML = "Please enter a 11 digit valid mobile number";
        error = true;
    }
    else{
        document.getElementById("mobile_error").innerHTML = "";
    }


    //EMAIL
    let atPos = email.indexOf('@');
    let dotPos = email.lastIndexOf('.');
    if(email === "")
    {
        document.getElementById("email_error").innerHTML = "Email is required";
        error = true;
    }
    else if(atPos <= 0 || dotPos <= 0 || (dotPos - atPos) <= 4 || dotPos == email.length - 1){
        document.getElementById("email_error").innerHTML = "Email is not valid!";
        error = true;
    }
    else{
        document.getElementById("email_error").innerHTML = "";
    }



    if(error)
    {
        return false;
    }
    else
    {
        return true;
    }
}