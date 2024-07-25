from django.shortcuts import render,redirect
from cart_app.cart import Cart
from payment_app.forms import ShippingForm, PaymentForm
from payment_app.models import ShippingAddress,Order, OrderItem
from django.contrib import messages
from django.contrib.auth.models import User 
from store_app.models import Product, Profile
import datetime
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Create your views here.

def orders(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        
        #get the order
        order = Order.objects.get(id=pk)
        #get tehr orders items
        items = OrderItem.objects.filter(order=pk)
        
        if request.POST:
            status = request.POST['shipping_status']
            #check if true or false
            if status == "true":
                #get the order
                order = Order.objects.filter(id=pk)
                #update the satus
                now = datetime.datetime.now()
                order.update(shipped=True, date_shipped=now)
            else:
                #get the order
                order = Order.objects.filter(id=pk)
                #update the satus
                order.update(shipped=False)
            messages.success(request, "Shipping status updated.....")
            return redirect('home')
        
        return render(request, "payment_app/orders.html", {"order":order, "items":items})
    else:
        messages.success(request, "Access Denied.....")
        return redirect('home')
    
    

def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        
        orders= Order.objects.filter(shipped=False)
        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            #check if true or false
            order = Order.objects.filter(id=num)
            #update the satus
            now = datetime.datetime.now()
            order.update(shipped=True, date_shipped=now)
           
            messages.success(request, "Shipping status updated.....")
            return redirect('home')
        
        
        
        
        
        return render(request, "payment_app/not_shipped_dash.html", {"orders":orders})
    else:
        messages.success(request, "Access Denied.....")
        return redirect('home')

def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders= Order.objects.filter(shipped=True)
        if request.POST:
            status = request.POST['shipping_status']
            num = request.POST['num']
            #check if true or false
            order = Order.objects.filter(id=num)
            #update the satus
            now = datetime.datetime.now()
            order.update(shipped=False)
           
            messages.success(request, "Shipping status updated.....")
            return redirect('home')
        return render(request, "payment_app/shipped_dash.html", {"orders":orders})
    else:
        messages.success(request, "Access Denied.....")
        return redirect('home') 

def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities= cart.get_quants
        totals = cart.cart_total()
        
        #get billing info from the last page
        payment_form=PaymentForm(request.POST or None)
        
        #get shipping session data stuff
        my_shipping = request.session.get('my_shipping')
        print(my_shipping)
        
        #gather order info
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        # create shipping address from session info
        
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        print(shipping_address)
        amount_paid = totals
                
        if request.user.is_authenticated:
            #logged in
            user = request.user
            #create order 
            create_order = Order(user=user,full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            
            #create order item 
            #get order id
            order_id= create_order.pk 
            #get product id info stuff
            for product in cart_products():
                #get product id
                product_id = product.id
                #get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                
                #get quantity
                
                for key,value in quantities().items():
                    if int(key) == product.id :
                        #value
                        #create orde item
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
                        print(create_order_item)
                        create_order_item.save()
                        
                        #files = request.FILES.getlist('files')
                        email_message = EmailMessage(
                        subject=f'Order Form: {full_name} - {email}',
                        #body=titulo_serie + " " + serie_o_pelicula + " " +  plataforma,
                        body=f"User ID: {user}\nOrder ID: {order_id}\nQuantity Value: {value}\nQuantities: {quantities().items()}\nTotals: {totals}\nProduct ID: {product_id}\nProduct Name: {product.name}\nItem Price: {price}\nShipping Address: {shipping_address}",
                
                        from_email=settings.EMAIL_HOST_USER,
                        to=['msb.duck@gmail.com', 'msb.tesla@gmail.com', 'msebti2@gmail.com', 'msb.acer@gmail.com'],
                        reply_to=['msebti2@gmail.com']
                    )
            
                        # Enviar el email
                        email_message.send(fail_silently=False)
            
            #delete our cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    #delete the key
                    del request.session[key]
                    
            #delete cart from db old carrt field
                        
            current_user = Profile.objects.filter(user__id=request.user.id)
            #delete shopping cart in DB old cart field
            current_user.update(old_cart="")
            
            
            messages.success(request, "Order Placed correctly.....")
            return redirect('home')
            
        else:
            #not logged in
             #create order 
            create_order = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            
             #create order item 
            #get order id
            order_id= create_order.pk 
            #get product id info stuff
            for product in cart_products():
                #get product id
                product_id = product.id
                #get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                
                #get quantity
                
                for key,value in quantities().items():
                    if int(key) == product.id :
                        #value
                        #create orde item
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
                        print(create_order_item)
                        create_order_item.save()
                        
                        #files = request.FILES.getlist('files')
                        email_message = EmailMessage(
                        subject=f'Order Form: {full_name} - {email}',
                        #body=titulo_serie + " " + serie_o_pelicula + " " +  plataforma,
                        body=f'Order ID: {order_id}\nQuantity Value: {value}\nQuantities: {quantities().items()}\nTotals: {totals}\nProduct ID: {product_id}\nProduct Name: {product.name}\nItem Price: {price}\nShipping Address: {shipping_address}',
                
                        from_email=settings.EMAIL_HOST_USER,
                        to=['msb.duck@gmail.com', 'msb.tesla@gmail.com', 'msebti2@gmail.com', 'msb.acer@gmail.com'],
                        reply_to=['msebti2@gmail.com']
                    )
            
                        # Enviar el email
                        email_message.send(fail_silently=False)
                        
            #delete our cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    #delete the key
                    del request.session[key]
            
                        
            messages.success(request, "Order Placed correctly.....")
            return redirect('home')
    
    else:
        messages.success(request, "Access Denied.....")
        
        return redirect('home')
        

def payment_success(request):
    
    return render(request, "payment_app/payment_success.html", {})

def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities= cart.get_quants
        totals = cart.cart_total()
        
        #create a session with shipping
        my_shipping =request.POST
        request.session['my_shipping'] = my_shipping
        
        #check to see if user is logged in
        if request.user.is_authenticated:
            billing_form = PaymentForm()
            context={'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_info':request.POST, 'billing_form': billing_form}
            return render(request, "payment_app/billing_info.html", context)
        else:
            # not logged in
            billing_form = PaymentForm()
            context={'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_info':request.POST, 'billing_form' : billing_form}
            return render(request, "payment_app/billing_info.html", context)
    
        shipping_form = request.POST
        context={'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form}
    
        return render(request, "payment_app/billing_info.html", context)
    else:
        messages.success(request, "Access Denied.....")
        
        return redirect('home')

    

def checkout(request):
     #get cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities= cart.get_quants
    totals = cart.cart_total()
    
    if request.user.is_authenticated:
        #check out as logged in user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        context={'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form}
        return render(request, "payment_app/checkout.html", context)
    else:
        #check out as guest
        shipping_form = ShippingForm(request.POST or None)
        context={'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form}
        return render(request, "payment_app/checkout.html", context)
    
    context={'cart_products':cart_products, 'quantities':quantities, 'totals':totals}
    
    return render(request, "payment_app/checkout.html", context)

