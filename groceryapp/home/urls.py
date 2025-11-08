
from django.urls import include, path
from home import views

urlpatterns = [
    path('',views.index),
    path('shop/',views.shop),
    path('shop-detail/<id>',views.shopdetail),
    path('contact/',views.contact),
    path('cart/',views.cart),
    path('login/',views.Login),
    path('check_login/',views.checklogin),
    path('dashboard/',views.dashboard),
    path('catogary/',views.catogary),
    path('catogaryedit/<id>',views.catogaryedit),
    path('catogarydelete/<id>',views.catogarydelete),
    path('addcatogary/',views.addcatogary),
    path('addcatogaryhandle/',views.addcatogaryhandle),
    path('handleedit/<id>',views.handleedit),
    path('brands/',views.brands),
    path('addbrand/',views.addbrand),
    path('addbrandhandle/',views.addbrandhandle),
    path('brandedit/<id>',views.brandedit),
    path('brandedithandle/<id>',views.brandedithandle),
    path('branddelete/<id>',views.branddelete),
    path('products/',views.products),
    path('addproduct/',views.addproduct),
    path('addproducthandle/',views.addproducthandle),
    path('productedit/<id>',views.productedit),
    path('productedithandle/<id>',views.productedithandle),
    path('productdelete/<id>',views.productdelete),
    path('logout/',views.Logout),
    path('addenquries/',views.addenquries),
    path('low_to_high/',views.low_to_high),
    path('high_to_low/',views.high_to_low),
    path('productsearch/',views.productsearch),

]
