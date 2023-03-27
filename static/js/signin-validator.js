function validate()
{
    const sic = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    
    //SIC
    if(sic === "")
    {
        document.getElementById("sic_error").innerHTML = "Mobile number is required";
        error = true;
    }
    else if(sic.length != 11 || isNaN(sic)){
        document.getElementById("sic_error").innerHTML = "Please enter a valid Mobile Number";
        error = true;
    }
    else{
        document.getElementById("sic_error").innerHTML = "";
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

}

