from store.forms.authforms import CustomerCreationForm, CustomerAuthform
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as loginuser, logout
from store.models import Tshirt, SizeVarient, Cart, Order, OrderItems, Payment,\
    Occasion,Brand,Colour,IdealFor,NeckType,Sleeve
from math import floor
from django.contrib.auth.decorators import login_required
from store.forms.checkout_form import CheckoutForm

from Tshirt_shop.settings import API_KEY, AUTH_TOKEN
from instamojo_wrapper import Instamojo

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


# Create your views here.















