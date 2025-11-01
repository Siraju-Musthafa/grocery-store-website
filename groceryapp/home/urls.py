
from django.urls import include, path
from home import views

urlpatterns = [
    path('',views.index),
    path('shop/',views.shop),
    path('shop-detail/',views.shopdetail),
    path('contact/',views.contact),
    path('cart/',views.cart),
    path('login/',views.Login),
    path('check_login/',views.checklogin),
    path('dashboard/',views.dashboard),
]
