# STORE URLS.PY

from django.contrib import admin
from django.urls import path

from store.views import home, cart, LoginView, signup, logout1, \
    checkout, validate_payment, ProductTemplateView,OrderListView
from store.views.cart import addtocart
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='homepage'),
    path('cart/',cart),
    path('order/',login_required(OrderListView.as_view(), login_url='/login/'),name = 'orders'),
    path('login/',LoginView.as_view(), name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout1),
    path('product/<str:slug>',ProductTemplateView.as_view()),
    path('addtocart/<str:slug>/<str:size>',addtocart),
    path('checkout/',checkout),
    path('validate_payment/',validate_payment),
]
