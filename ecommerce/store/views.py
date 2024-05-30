from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html' , context)

def checkout(request):
    items = []
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    
    else:
        items = []
        order = {'cart_total_number':0, 'cart_total_price':0}

        
    context = {'items':items, 'order':order}
    return render(request,'store/checkout.html' , context)

def cart(request):
    items = []
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    
    else:
        items = []
        order = {'cart_total_number':0, 'cart_total_price':0}

        
    context = {'items':items, 'order':order}

    return render(request,'store/cart.html' , context)