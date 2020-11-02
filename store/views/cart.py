from store.forms.authforms import CustomerCreationForm, CustomerAuthform
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as loginuser, logout
from store.models import Tshirt, SizeVarient, Cart, Order, OrderItems, Payment,\
    Occasion,Brand,Colour,IdealFor,NeckType,Sleeve
from math import floor
from django.contrib.auth.decorators import login_required
from store.forms.checkout_form import CheckoutForm


def cart(request):
    cart = request.session.get('cart')
    if cart is None:
        cart = []

    for c in cart:
        tshirt_id = c.get('tshirt')
        tshirt = Tshirt.objects.get(id=tshirt_id)
        c['size'] = SizeVarient.objects.get(tshirt=tshirt_id, size=c['size'])
        c['tshirt'] = tshirt
    return render(request, template_name='store/cart.html', context={'cart': cart})

def addtocart(request, slug, size):
    user = None
    if request.user.is_authenticated:
        user = request.user

    cart = request.session.get("cart")

    if cart is None:
        cart = []

    tshirt = Tshirt.objects.get(slug=slug)
    add_cart_to_anom_user(cart, size, tshirt)
    if user is not None:
        add_cart_to_database(user, size, tshirt)

    request.session['cart'] = cart
    return_url = request.GET.get('return_url')
    return redirect(return_url)


def add_cart_to_database(user, size, tshirt):
    size = SizeVarient.objects.get(size=size, tshirt=tshirt)
    existing = Cart.objects.filter(user=user, sizevarient=size)
    if len(existing) > 0:
        obj = existing[0]
        obj.quantity = obj.quantity + 1
        obj.save()
    else:
        c = Cart()
        c.user = user
        c.sizevarient = size
        c.quantity = 1
        c.save()


def add_cart_to_anom_user(cart, size, tshirt):
    flag = True
    for cart_obj in cart:
        t_id = cart_obj.get('tshirt')
        size_short = cart_obj.get('size')
        if t_id == tshirt.id and size == size_short:
            flag = False
            cart_obj['quantity'] = cart_obj['quantity'] + 1
    if flag:
        cart_obj = {
            "tshirt": tshirt.id,
            "size": size,
            "quantity": 1
        }
        cart.append(cart_obj)

