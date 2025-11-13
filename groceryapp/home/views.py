from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import productstable, Cart, Order
import razorpay
razorpay_client = razorpay.Client(auth=('rzp_test_9zruMnoLDlsCLG','oXUZ9Mf5zhjoZsTFLc7RpABO'))
# Create your views here.
def index(request):
    data=productstable.objects.all()
    return render(request,"index.html",{'data':data})

def shop(request):
    data=productstable.objects.all()
    cart=Cart.objects.filter(user=request.user)
    lencart=len(cart)
    catogary=catogarytable.objects.annotate(product_count=Count('productstable'))

    return render(request,'shop.html',{'data':data,'length':lencart,'catogary':catogary})

def shopdetail(request,id):
    product=productstable.objects.get(id=id)
    catogary=catogarytable.objects.annotate(product_count=Count('productstable'))
    related=productstable.objects.filter(catogary=product.catogary.id)
    return render(request,'shop-detail.html',{'data':product,"catogary":catogary,'related':related})

def contact(request):
    return render(request,'contact.html')

def cart(request):
     cart=Cart.objects.filter(user=request.user)
     lencart=len(cart)
     return render(request,'cart.html',{'length':lencart})

def Login(request):
    return render(request,'login.html')

def  checklogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
           login(request,user)
           if user.username=='admin':
              return redirect('/dashboard',{'user':user})
           else:
               return redirect('/')
        else:
             return redirect('/login/')

def dashboard(request):
    return render(request,'dashboard.html')  

def catogary(request):
    data=catogarytable.objects.all()
    return render(request,'catogary.html',{'data':data}) 

def catogaryedit(request,id):
    data=catogarytable.objects.get(id=id)
    return render(request,'catogaryedit.html',{'data':data})

def handleedit(request,id):
     obj=catogarytable.objects.get(id=id)
     obj.catogaryname=request.POST.get('catogaryname')
     obj.catogarystatus=request.POST.get('status')
     if request.FILES.get('image'):
        obj.catogaryimage=request.FILES.get('image')
     obj.save()
     return redirect('/catogary/')
    
def catogarydelete(request,id):
    data=catogarytable.objects.get(id=id)
    data.delete()
    return redirect('/catogary/')

def addcatogary(request):
    return render(request,'addcatogary.html')

def addcatogaryhandle(request):
    if request.method=='POST':
      obj=catogarytable()
      obj.catogaryname=request.POST.get('catogaryname')
      obj.catogaryimage=request.FILES.get('image')
      obj.catogarystatus=request.POST.get('status')
      obj.save()

    return redirect('/dashboard/')

def brands(request):
    data=brandstable.objects.all()
    return render(request,'brands.html',{'data':data})

def addbrand(request):
    return render(request,'addbrand.html')

def addbrandhandle(request):
    if request.POST:
        obj=brandstable()
        obj.brandname=request.POST.get('name')
        obj.brandimage=request.FILES.get('image')
        obj.brandstatus=request.POST.get('status')
        obj.save()
    
    return redirect('/brands/')

def brandedit(request,id):
    data=brandstable.objects.get(id=id)
    return render(request,'brandedit.html',{'data':data})

def brandedithandle(request,id):
    obj=brandstable.objects.get(id=id)
    obj.brandname=request.POST.get('name')
    obj.brandstatus=request.POST.get('status')
    if request.POST.get('image'):
        obj.brandimage=request.POST.get('image')
    obj.save()
    return redirect('/brands/')

def branddelete(request,id):
    data=brandstable.objects.get(id=id)
    data.delete()
    return redirect('/brands/')

def products(request):
    data=productstable.objects.all()
    return render(request,"products.html",{'data':data})

def addproduct(request):
    brands=brandstable.objects.filter(brandstatus="Active")
    catogary=catogarytable.objects.filter(catogarystatus='Active')

    return render(request,'addproduct.html',{"brands":brands,'catogary':catogary})

def addproducthandle(request):
    if request.POST:
        obj=productstable()
        obj.name=request.POST.get('name')
        obj.image=request.FILES.get('image')   
        obj.description=request.POST.get('description')
        obj.brand_id=request.POST.get('brands')
        obj.our_price=request.POST.get('ourprice')
        obj.orginal_price=request.POST.get('orginalprice')
        obj.tax_amount=request.POST.get('taxamount')
        obj.open_stock=request.POST.get('openstock')
        obj.current_stock=request.POST.get('currentstock')
        obj.catogary_id=request.POST.get('catogary')
        obj.status=request.POST.get('status')
        obj.save()
    return redirect('/products/')   

def productedit(request,id):
    data=productstable.objects.get(id=id)
    return render(request,'productedit.html',{'data':data})

def productedithandle(request,id):
    data=productstable.objects.get(id=id)
    if request.POST:
         data.name=request.POST.get('name')
         data.description=request.POST.get('discription')
         data.brand=request.POST.get('brand')
         data.status=request.POST.get('status')
         if request.FILES.get('image'):
            data.image=request.FILES.get('image')

    data.save()
    return redirect('/products/')

def productdelete(request,id):
    data=productstable.objects.get(id=id)
    data.delete()
    return redirect('/products/')


def Logout(request):
    logout(request)
    return redirect('/')

def addenquries(request):
    if request.POST:
       obj=enquiries()
       obj.Name=request.POST.get('name')
       obj.email=request.POST.get('email')
       obj.message=request.POST.get('message')
       obj.save()
       return redirect('/contact/')
    
    
def low_to_high(request):
    data=productstable.objects.all().order_by('our_price')
    catogary=catogarytable.objects.annotate(product_count=Count('productstable')) 
    return render(request,'shop.html',{'data':data,'catogary':catogary})

def  high_to_low(request):
    data=productstable.objects.all().order_by('-our_price')
    catogary=catogarytable.objects.annotate(product_count=Count('productstable'))
     
    return render(request,'shop.html',{'data':data,'catogary':catogary})

def productsearch(request):
     keyword=request.GET.get('search')
     products=productstable.objects.all()
     catogary=catogarytable.objects.annotate(product_count=Count('productstable'))

     
     if keyword:
        products = products.filter(
            Q(name__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(brand__brandname__icontains=keyword) |
            Q(catogary__catogaryname__icontains=keyword)
        )
     return render(request,'shop.html',{'data':products,'catogary':catogary})    
     
def vegsearch(request):
    # products=productstable.objects.filter(catogary='vegitable') 
    return render(request,"trdf.html",{'data':products})

def fruitssearch(request):
    fruitscatogary=catogarytable.objects.get(catogaryname='fruits')
    products=productstable.objects.filter(catogary=fruitscatogary) 
    print(products)
    print('hello siraj')
    return render(request,"shop.html",{'data':products})



@login_required
def add_to_cart(request, product_id):
   # product = get_object_or_404(productstable, id=product_id)
    product=productstable.objects.get(id=product_id)

   
    if product.status=='Active':
        if  Cart.objects.filter(user=request.user,product_id=product_id):
             cart=Cart.objects.get(user=request.user,product=product)
             cart.quantity= cart.quantity+1
             cart.save()
             return redirect('/view_cart/')
        else:
            if product.current_stock>=0:
                Cart.objects.create(user=request.user,product_id=product_id)
                messages.success(request, "product added in cart!")
    return redirect('view_cart')


@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


@login_required
def checkout(request):
        cart_items = Cart.objects.filter(user=request.user)
        cart=len( cart_items)
        total = sum(item.total_price() for item in cart_items)
    
        order = Order.objects.create(user=request.user, total_amount=total)
        order.products.set(cart_items)
        cart_items.delete()
        currency = "INR"
        amount = int(total * 100) 
        razorpay_order=razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = 'rzp_test_9zruMnoLDlsCLG'
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['data']=order
        context['cart']=cart
        context['total']=total
        return render(request, 'checkout.html',context)
    

    
    #return render(request, 'checkout.html', {'cart_items': cart_items, 'cart':cart,'total': total})

def paymenthandler(request):
        razorpay_order_id = request.POST.get('order_id')
        payment_id = request.POST.get('payment_id', '')      
        amount = int(request.POST.get('amount',0))
        try:
            razorpay_client.payment.capture(payment_id, amount)
            obj=orderupdates()
            obj.orderid=razorpay_order_id
            obj.amount=int(amount)/100
            obj.paymentid=payment_id
            obj.save()
            return redirect('/payment_success/')
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Signature verification failed.")
        except razorpay.errors.BadRequestError as e:
            print("Bad Request Error:", e)
            return HttpResponseBadRequest(f"Payment capture failed: {e}")
        except Exception as e:
            print("Unexpected error:", e)
            return HttpResponseBadRequest(f"Server error: {e}")
   
def removecart(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    return redirect('/cart/')

def ordersuccess(request):
    return render(request,'order_success.html')