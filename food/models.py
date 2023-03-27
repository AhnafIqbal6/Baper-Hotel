from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User      # for Order class

# Create your models here.

class Cuisine(models.Model):
    category = models.CharField(max_length = 100)   # CharField means varchar
    # category is the column name
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category


class Food(models.Model):
    category = models.ForeignKey(Cuisine, on_delete=models.DO_NOTHING)  #if parent data gets deleted, we can still use the data through DO_NOTING 
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    secondary_description = models.TextField(blank=True)    #optional, so we make blank = true means we may or may not give data in this field
    is_available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to = 'food_images/')   # a new folder is created under CAFE

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)     # Order table has foreign key relationship with User table
    order_details = models.CharField(max_length=500)
    total_price = models.FloatField()
    is_ready = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username       # converting username to string type

