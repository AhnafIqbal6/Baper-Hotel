from django.urls import path

from . import views


urlpatterns=[
    path('signup/', views.signup, name="signup"),   # <form action="{% url 'signup' %}" in templates > user > signup.html
    path('signin/', views.signin, name="signin"),   # <form action="{% url 'signin' %}" in templates > user > signin.html
    path('signout/', views.signout, name="signout"),
]