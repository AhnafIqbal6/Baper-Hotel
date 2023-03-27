from django.contrib import admin

# Register your models here.

from .models import Cuisine, Food, Order

class CuisineAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_at')   # to display category and created_at attributes to the admin in admin page under Cuisine table
    ordering = ('category',)                    # ordering will be based on category (alphabetical order)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')   # to display name, price, is_available columns to the user
    ordering = ('name',)                        # ordering will be on the basis of name
    list_editable = ('is_available',)           # to add check boxes, for single items we add a comma
    search_fields = ('name',)                   # to add a search field, for single items we add a comma
    list_filter = ('is_available',)             # to add a filter on right side, for single items we add a comma


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_details', 'is_ready', 'is_delivered')  # to display id, user, order_details, is_ready, is_delivered columns to the admin in admin page under Orders table
    list_editable = ('is_ready' , 'is_delivered')       # for check boxes
    ordering = ('-id', )                              # for single items we add a comma , -id means ordering will be in descending order


admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)



