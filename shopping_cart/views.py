from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


# from accounts.models import Profile
# from products.models import Product
#
# from shopping_cart.extras import generate_order_id, transact, generate_client_token
# from shopping_cart.models import OrderItem, Order, Transaction
#
# import datetime
# import stripe