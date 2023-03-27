from django.shortcuts import render, redirect
from .utils import customSendMail
# to interact with the database, views uses models as models interact with the database
from .models import Food, Order             # so from models we import the Food table and Order table

from random import randint                  # to generate random integer for OTP
from django.contrib import messages         # to generate error/success message 


# this function is called when menu is clicked in the navbar

def menu(request):
    foods = Food.objects.all()         # foods is an object, Food.objects.all() is same as select * from Food
    context = {                        # we create a dictionary context which stores the foods object 
        'foods': foods
    }
    return render(request, 'food/menu.html', context)   # we pass this context dictionary to menu.html in food folder under templates, this foods object can be used to directly fetch values from Food table



# this function is called when in menu page a particular item's details button is clicked

def details(request, id):
    food = Food.objects.get(id = id)  # first id is the column name, second id is the request id we received, e.g., select * from Food where id = 3
    context = {
        'food' : food                   # food is the object of the Food table for the particular food items whose details button we have clicked in menu.html
    }
    return render(request, 'food/details.html', context)



# this function is clicked when Add to Cart button is clicked in details.html page, it receives the food item selected (i.e, id) and its quantity

def add_to_cart(request):
    if request.method == "POST":
        food_id = request.POST.get("food_id")  # food_id is the local variable, "food_id" is the id of selected (add to cart) item     
        quantity = request.POST.get("quantity")

        items = {}                              # items is a dictionary

        if request.session.get("food_items"):   # if some althis will store previously add to cart items also, if we dont write we will lose the data of previously added item when we add a new item to cart
            items = request.session.get("food_items")

        items[food_id] = quantity               # inserting into dict, items = {"food_id" : quantity}

        request.session["food_items"] = items   # creating a food_items session variable to store the dictionary value temporarily, as html is volatile, session will preserve all the request data

        print(request.session["food_items"])    # printing in terminal for cross check
    
    return redirect('cart')                     # once add to cart button is clicked, control flows to cart.html page




def cart(request):
    foods = request.session.get("food_items")

    # we will pass id, name of food, quantity, price and photo of each id that is added to cart by user
    items = []                                  #  dictionary to our cart.html page
    total_price = 0

    if foods:                                   # if some item is added to cart
        for id, quantity in foods.items():      # foods is a dictionary which contains id and qty of each item added to cart
            food = Food.objects.get(id = id)    # 1st id is the col name of Food table, 2nd id is the for loop varibale, food is the object which stores all details of the item whose col id = id of food selected
            price = int(quantity) * int(food.price)     # converting quantity and price to int as they are in string types {'id' : 'quantity'}, food.price fetches the price
            total_price += price
            items.append({
                "id" : id, 
                "name" : food.name,
                "quantity" : quantity,
                "price" : price,
                "photo" : food.photo
            })
    context = {
        "foods" : items, 
        "total_price" : total_price
    }

    return render(request, 'food/cart.html', context)




# this function is called when we click on delete button of an item

def delete_cart_item(request, id):
    foods = request.session.get("food_items")    # storing the food_items session variable in foods dictionary
    del foods[id]                                 # deleting the food of the id received 
    request.session["food_items"] = foods       # updating session variable after deleting the food

    return redirect('cart')



# this will generate otp


def check_out(request):
    if not request.session.get("OTP"):      # if otp is not generated at all then this is executed
        otp = randint(111111, 999999)    # generating a random integer for otp, randint is imported
        customSendMail(                          # send_mail is imported
            "OTP from Baper Hotel",         # subject of email
            f"Your OTP to order food from Baper Hotel is {otp}",  #msg
            request.user.email              # recipient email, the mail id of the logged in user
        )
        request.session["OTP"] = otp
    return render(request, 'food/check_out.html')




# this function verifies the otp entered by user, if generated otp and entered otp is same render to orders.html else generate error "Invalid OTP" and redirect to check_out.html

def place_order(request):
    if request.method == "POST":
        otp = int(request.POST.get("otp"))  # "otp" is the id of the input field and we are fetching the otp entered by user and storing in local varible otp
        if int(request.session.get("OTP")) != int(otp):      # type cast the otp to integer as the input filed will give string type and match it with the otp generated during the session
            messages.error(request, "Invalid OTP")      # if otp does not match then show msg invalid otp
            return redirect("check_out")

        else:
            foods = request.session.get("food_items")   # storing food_items session variable in foods dictionary
            if foods:                                   # if foods contain atleast one item
                order_details = ""                      # local variables
                total_price = 0

                for id, quantity in foods.items():          
                    food = Food.objects.get(id = id)    # fetching the id of the food added in cart from Food table
                    price = food.price * int(quantity)  # calculating the price
                    total_price += price                # updating total price
                    order_details += f"{food.name} x {quantity} , "    # order_details string variable will store food name into quantitiy

                order = Order(user = request.user, order_details = order_details, total_price = total_price) # creating object order of Order table, requset.user is the logged in user's id
                # first order_details is the column name of Order table, second order_details is the local variable
                order.save()                # saving the details (id, user, order_details) in Order table 

                del request.session["food_items"]       # once the order is placed by verifying the otp, we will clear the cart and cart details are in food_items session variable, so we delete it
                del request.session["OTP"]              # we will also delete the otp stored in session variable OTP

    return redirect('orders')         # if otp verified then redirect to orders.html




def orders(request):
    orders = Order.objects.filter(user = request.user).order_by("-id")  # creating object of Order table named as orders where id = id of the logged in user, -id means sort in decreasing order of id, i.e., latest order will be at top
    context = {
        "orders" : orders
    }

    return render(request, 'food/orders.html', context)     # passing this context dictionary to orders.html page in food folder under templates, there we can use the orders object to fetch data directly from Order table




# for the search bar, we render to search

def search(request):
    if request.method == "POST":            # this form is in base.html for the search bar
        name = request.POST.get('form1')     # name is the local variable, the name of input field for search bar in base.html is 'form1', we are fetching the value entered in the search box and storing in name variable 

        if Food.objects.filter(name = name).exists():       # if any food of such name exists, then we create a object of the same food item
            foodname = Food.objects.get(name = name)        # foodname is the object, 1st name is the col name of Food tabkle, 2nd name is the local variable

        else:                                               # if no such food exits, we generate an error msg and render the request to search.html
            messages.error(request, "no such food item")
            return render(request, 'food/search.html')

    context = {                        # we create a dictionary context which stores the foodname object 
        'foodname' : foodname
    }
    return render(request, 'food/search.html', context)     # we pass this dictionary to search.html, there we can use foodname object to fetch values from Food table

