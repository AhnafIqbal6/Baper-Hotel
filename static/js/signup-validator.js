function validate()
{
    const firstname = document.getElementById('first_name').value;
    const lastname = document.getElementById('last_name').value;
    const sic = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const password2 = document.getElementById('password2').value;
    let error  = false;


    //NAME
    if(firstname === "")
    {
        //console.log("Name is required");
        document.getElementById("firstname_error").innerHTML = "Name is required!";
        error = true;
    }
    else{
        document.getElementById("firstname_error").innerHTML = "";
    }

    if(lastname === "")
    {
        //console.log("Name is required");
        document.getElementById("lastname_error").innerHTML = "Name is required!";
        error = true;
    }
    else{
        document.getElementById("lastname_error").innerHTML = "";
    }



    //SIC
    if(sic === "")
    {
        document.getElementById("sic_error").innerHTML = "SIC number is required";
        error = true;
    }
    else if(sic.length != 11 || isNaN(sic)){
        document.getElementById("sic_error").innerHTML = "Please enter a valid SIC";
        error = true;
    }
    else{
        document.getElementById("sic_error").innerHTML = "";
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


    //PASSWORD
    if(password === "")
    {
        document.getElementById("password_error").innerHTML = "Password is required !";
        error = true;
    }
    else if(password.length <= 8 || password.length > 16)
    {
        document.getElementById("password_error").innerHTML = "Password must be 8 - 16 characters long";
        error = true;
    }
    else if(!password.match(/[a-z]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a lowercase character";
        error = true;
    }
    else if(!password.match(/[A-Z]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a uppercase character";
        error = true;
    }
    else if(!password.match(/[0-9]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a number";
        error = true;
    }
    else if(!password.match(/[!@#$%^&*]/)){
        document.getElementById("password_error").innerHTML = "Password must contain a character among !@]#$%^&*";
        error = true;
    }
    else{
        document.getElementById("password_error").innerHTML = "";
    }



    // CONFIRM PASSWORD
    if(password2 === "")
    {
        document.getElementById("password2_error").innerHTML = "confirm password is required !";
        error = true;
    }
    else if(password != password2)
    {
        document.getElementById("password2_error").innerHTML = "password and confirm password must be same";
        error = true;
    }
    else{
        document.getElementById("password2_error").innerHTML = "";
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