from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store_app.models import Product
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.


def cart_summary(request):
    #get cart
    cart = Cart(request)
    cart_products = cart.get_prods
    
    quantities= cart.get_quants
    totals = cart.cart_total()
    context={'cart_products':cart_products, 'quantities':quantities, 'totals':totals}
    return render(request, "cart_app/cart_summary.html", context)

def cart_add(request):
    #get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #save to session
        cart.add(product=product, quantity=product_qty)
        
        #get cart quantity
        
        cart_quantity = cart.__len__()
        
        # return response
        
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product added to the cart....."))
        
        return response
    
        #sessionid:"xbrldqvsbgam8ad2230vn4d1wh381bnf"

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        #call delete funcion
        
        cart.delete(product=product_id)
        
        response = JsonResponse({'product': product_id})
        messages.success(request, ("Items deleted form shopping cart....."))
        return response



def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        
        response = JsonResponse({'qty': product_qty})
        messages.success(request, ("Your cart has been updated....."))
        
        return response
        #return redirect('cart_summary')

#sessionid:"x0t12a8c335xpc4lwras1i60tt22enk6"
#x0t12a8c335xpc4lwras1i60tt22enk6
