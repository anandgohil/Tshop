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


def validate_payment(request):
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    print(payment_request_id,payment_id)
    response = api.payment_request_payment_status(payment_request_id, payment_id)

    print(response['payment_request']['purpose']) # Purpose of Payment Request
    status = response.get('payment_request').get('payment').get('status')

    if status != 'Failed':
        user = None
        if request.user.is_authenticated:
            user = request.user
        print('user is',user)
        try:
            payment = Payment.objects.get(payment_request_id=payment_request_id)
            payment.payment_id = payment_id
            payment.Payment_status = status
            payment.save()

            order = payment.order
            order.order_status = 'PLACED'
            order.save()

            cart=[]
            request.session['cart'] = cart

            Cart.objects.filter(user=user).delete()


            return redirect('orders')
        except:
            return render(request,'store/payment_failed.html')
    else:
        return render(request, 'store/payment_failed.html')
    return HttpResponse(status)