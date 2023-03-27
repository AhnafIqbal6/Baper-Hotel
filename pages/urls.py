# app url

from django.urls import path
from . import views             # to access the index function which is in views.py, we import the views file from root '.' dir

urlpatterns = [
    # path('index/', views.index, name='home'), we have removed this request (index/) because, if we keep this and in address bar we search localhost:8000, we will get an error page and we have to write localhost:8000/index/ everytime to access the index page
    path('', views.index, name='home'),             # for a proper convention, whenever we will search localhost:8000, directly we will be redirected to index page
    path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact'),
    
]