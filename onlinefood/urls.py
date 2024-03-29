from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('cart',views.cart,name='cart'),
    path('logout',views.logout_user,name='logout'),
    path('checkout',views.checkout,name='checkout')
]