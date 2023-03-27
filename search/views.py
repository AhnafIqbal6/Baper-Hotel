from django.shortcuts import render
from food.models import Food
from django.http import JsonResponse
# Create your views here.

def suggestions(request,key):
    foods= False
    try:
        foods= []
        all= Food.objects.filter(name__icontains=key)[0:6]
        for item in all:
            foods.append({"name":item.name,"id":item.id})
    except:
        pass
    return JsonResponse(foods,safe=False)