from django.shortcuts import render, redirect
from store.models import SizeVarient, Order, OrderItems, Payment
from math import floor
from django.contrib.auth.decorators import login_required
from store.forms.checkout_form import CheckoutForm
from Tshirt_shop.settings import API_KEY, AUTH_TOKEN
from instamojo_wrapper import Instamojo

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


# UTILITY function
def cal_total_payable_amount(cart):
    total = 0
    for c in cart:
        # print(c.get('tshirt').discount)
        discount = c.get('tshirt').discount
        # print(discount)
        price = c.get('size').price
        sale_price = floor(price - (price * (discount / 100)))
        total_of_single_product = sale_price * c.get('quantity')
        total = total + total_of_single_product
    return total


@login_required(login_url='/login/')
def checkout(request):
    if request.method == "GET":
        form = CheckoutForm()
        cart = request.session.get('cart')

        if cart is None:
            cart = []

        for c in cart:
            size_str = c.get('size')
            tshirt_id = c.get('tshirt')
            size_obj = SizeVarient.objects.get(size=size_str, tshirt=tshirt_id)
            c['size'] = size_obj
            c['tshirt'] = size_obj.tshirt
        context = {'form': form, 'cart': cart}

        return render(request, template_name="store/checkout.html", context=context)
    else:
        form = CheckoutForm(request.POST)
        user = None
        print("user 11",user)
        if request.user.is_authenticated:
            print("user 12", user)
            user = request.user
        if form.is_valid():
            print("user 13", user)
            # payment
            cart = request.session.get('cart')
            if cart is None:
                cart = []
            for c in cart:
                size_str = c.get('size')
                tshirt_id = c.get('tshirt')
                size_obj = SizeVarient.objects.get(size=size_str, tshirt=tshirt_id)
                c['size'] = size_obj
                c['tshirt'] = size_obj.tshirt
            shipping_addres = form.cleaned_data.get('shipping_addres')
            contact = form.cleaned_data.get('contact')
            payment_method = form.cleaned_data.get('payment_method')
            total = cal_total_payable_amount(cart)

            print(shipping_addres, contact, payment_method, total)

            order = Order()
            order.shipping_addres = shipping_addres
            order.contact = contact
            order.payment_method = payment_method
            order.total = total
            order.order_status = "PENDING"
            order.user = user
            order.save()

            # saving order_items
            for c in cart:
                order_item = OrderItems()
                order_item.order = order
                size = c.get('size')
                tshirt = c.get('tshirt')
                order_item.price = floor(size.price - (size.price * (tshirt.discount) / 100))
                order_item.quantity = c.get('quantity')
                order_item.size = size
                order_item.tshirt = tshirt
                order_item.save()

            # payment gateway
            response = api.payment_request_create(
                amount=order.total,
                purpose='Payment for tshirt',
                send_email=True,
                buyer_name= f'{user.first_name} {user.last_name}',
                email=user.email,
                redirect_url="http://127.0.0.1:8000/validate_payment"
            )
            # print('response', response)
            print('request_id',response['payment_request']['id'])
            print('request_longurl',response['payment_request']['longurl'])

            payment_id = (response['payment_request']['id'])
            url = response['payment_request']['longurl']

            payment = Payment()
            payment.order = order
            payment.payment_request_id = payment_id
            payment.save()
            return redirect(url)

        else:
            return redirect('/checkout/')
