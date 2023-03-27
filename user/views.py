from django.shortcuts import render, redirect

from django.contrib.auth.models import User         # importing User models

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):                                # this function is called when we click signup button in sigup.html page, flow goes from signup.html's form action = {% url 'signup' %} to urls.py of user app to this function
    if request.method == "POST":
        f_name = request.POST.get('first_name')     # here first_name is the name of the input field 'first_name' in signup.html 
        l_name = request.POST.get('last_name')      # l_name is the local variable, note-> last_name is the name of the input field not he id of input field in signup.html form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f_name, l_name, username, email, password)    # printing in terminal

        error = False       # for handling multiple errors


        # this if is executed when a already existing username is entered by user
        if User.objects.filter(username = username).exists():
            print("Mobile Number already registered")                          # printing a message in terminal
            messages.error(request, "Mobile Number already registeredn")
            error = True


        # this if is executed when a already existing email is entered by user
        if User.objects.filter(email = email).exists():
            print("EMAIL already taken")
            messages.error(request, "Email already taken")
            error = True

        if error:
            return render(request, 'user/signup.html')      # request is rendered to the same page 

        # creating object
        # we are using try except block because if we donot write this and give a sic which is already registered then it will redirect to an error page, so to avoid the error page we use try except, if sic is already registered then expect block will handle it
        try:
            user = User.objects.create_user(    # create_user is inbuilt function
                first_name = f_name,            # first_name is the column name of User table
                last_name = l_name,
                username = username,
                email = email,
                password = password

            )

            user.save()     # saving the object into database

            # if new user is created successfully then we display the success message as written and redirect to signin.html page
            messages.success(request, "Account created successfully. Login to continue.")
            return redirect('signin')
        except Exception as e:
            print(e)

    return render(request, 'user/signup.html')


# this function is called when sign in btn is clicked in signup.html

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')     # username is the local variable, 'username' is the name of the input field in signin.html's <form> not the id
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)     # returns None, not None , first username is the column name and 2nd one is the local variable

        if user is not None:            # if existing user
            login(request, user)        # creates a session 
            return redirect('menu')     # redirect to menu.html 

        else:
            messages.error(request, "Invalid Credentials")


    return render(request, 'user/signin.html')


def signout(request):
    logout(request)                 # session is expired, logout is inbuilt function
    return redirect('signin')       # once logged out, redirect to signin page