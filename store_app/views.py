from django.shortcuts import render,redirect
from .models import Product,Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,UpdateUserForm,ChangePasswordForm, UserInfoForm
from django import forms
from django.db.models import Q
import json
from cart_app.cart import Cart
from payment_app.forms import ShippingForm
from payment_app.models import ShippingAddress

# Create your views here.

def search(request):
    #determine if they filled out the form 
    
    if request.method == 'POST':
        searched = request.POST['searched']
        #query the products db model
        
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        
        #test for null
        
        if not searched:
            messages.success(request, "That Product does not xist please try again....")
            return render(request, 'store_app/search.html',{})
        else:
            context={'searched':searched}
            return render(request, 'store_app/search.html',context)
    else:
        return render(request, 'store_app/search.html',{})
    
    
    
    

def update_info(request):
    if request.user.is_authenticated:
        #get current user
        current_user= Profile.objects.get(user__id=request.user.id)
        #get current user shipping info
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        
        #get original user form
        form = UserInfoForm(request.POST or None, instance=current_user)
        
        #get user orignal shipping form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        
        
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "Your Info has been Updated....")
            return redirect('home')
        
            
        context={'form':form, 'shipping_form':shipping_form}
        
        return render(request, 'store_app/update_info.html',context)
    else:
        messages.success(request, "You must be logged in to access this page.......")
        return redirect('home')

def update_password(request):
    
    if request.user.is_authenticated:
        current_user=request.user
        #did the fill out the form
        if request.method == 'POST':
            foo = current_user
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been update please log in again Thank you....")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')    
                    
        
        else:
            form = ChangePasswordForm(current_user)
            context={'form':form}
            return render(request, 'store_app/update_password.html',context)
    else:
        messages.success(request, "You must be logged in to view that page....")
        return redirect('home')

def update_user(request):
    
    if request.user.is_authenticated:
        current_user= User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "User has been Updated....")
            return redirect('home')
        
            
        context={'user_form':user_form}
        
        return render(request, 'store_app/update_user.html',context)
    else:
        messages.success(request, "You must be logged in to access this page.......")
        return redirect('home')

def category_summary(request):
    categories = Category.objects.all()
    context={'categories':categories}
    return render(request, 'store_app/category_summary.html',context)

def category(request, foo):
    foo = foo.replace('-', ' ')
    #grab the category from url
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        context={'products':products, 'category': category}
        return render(request, 'store_app/category.html',context)
    
    except:
        messages.success(request, ("That Cagegory Doesn't exist Sorry......"))
        return redirect('home')
    
    
    
    

def product(request, pk):
    product= Product.objects.get(id=pk)
    context={'product':product}
    return render(request, 'store_app/product.html',context)
    

def home(request):
    products= Product.objects.all()
    context={'products':products}
    return render(request, 'store_app/home.html',context)

def about(request):
    context={}
    return render(request, 'store_app/about.html',context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # do some shopping cart stuff
            
            current_user = Profile.objects.get(user__id=request.user.id)
            #get ther saved cart from DB
            saved_cart = current_user.old_cart
            #convert db string to python diccionary
            
            if saved_cart:
                #convert to diccionary usin json 
                converted_cart=json.loads(saved_cart)
                #add loaded dic to sesssion
                cart = Cart(request)
                
                #loop throw the cart and items form db
                
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)
                    
            
            
            messages.success(request, ("You have been logged In"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again later Thanks....."))
            return redirect('login')
    else:
        context={}
        return render(request, 'store_app/login.html',context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out ... Thanks for stopping by"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("User Created - Please Fill out Your user infoo Below thank you....."))
            return redirect('update_info')
        
        else:
            messages.success(request, ("Whoops there was a problem registering try again please....."))
            
            return redirect('register')
    else:
        context={'form':form}
        return render(request, 'store_app/register.html',context)
    
    