from django.urls import path
from . import views             # to access the all the functions which is in views.py, we import the views file from root '.' dir

urlpatterns = [
    path('menu/', views.menu, name="menu"),                     # for base.html <a href="{% url 'menu'%}"
    path('details/<int:id>/', views.details, name="details"), # for menu.html <a href="{% url 'details' food.id %}"     <int:id> is the request that is generated when we click the details button a particular item in menu.html
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),    # for details.html form action="{% url 'add_to_cart' %}"
    path('cart/', views.cart, name="cart"),                         # for base.html <a href="{% url 'cart' %}"
    path('delete_cart_item/<str:id>/', views.delete_cart_item, name="delete_cart_item"), # id is string type so <str:id>
    path('check_out/', views.check_out, name="check_out"),          # for cart.html a href = "{% url 'check_out' %}", line 37
    path('place_order/', views.place_order, name="place_order"),    # for check_out.html form action = "{% url 'place_order' %}"
    path('orders/', views.orders, name="orders"),                   # this request ius generated when a logged in user clicks order in dropdown for base.html
    path('search/', views.search, name='search'),                   # this request is generated for search bar in base.html
]