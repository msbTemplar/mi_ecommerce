from store_app.models import Product,Profile

class Cart():
    def __init__(self, request) :
        self.session=request.session
        # get request
        self.request = request
        #get the current session key if it exist
        
        cart = self.session.get('session_key')
                                
        # if the user us new no session kley create one)
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # male sure cart is available on all pages of our site
        
        self.cart = cart 
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        # logic 
        
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
        # deal whith logged in user
        
        if self.request.user.is_authenticated:
            #get the curret user profile
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert to {'3':1} to {"3":1}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # Save our carty to the profile model
            
            current_user.update(old_cart=str(carty))
        
    
       
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # logic 
        
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
        # deal whith logged in user
        
        if self.request.user.is_authenticated:
            #get the curret user profile
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert to {'3':1} to {"3":1}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # Save our carty to the profile model
            
            current_user.update(old_cart=str(carty))
                
        #sessionid:"31sewhrh7670ekdlsim4o7ih5a80vixu"
    
    def cart_total(self):
        #get product id
        product_ids=self.cart.keys()
        #lookup tose keys in db product
        products=Product.objects.filter(id__in=product_ids)
        #get quantities
        quantities = self.cart
        #start countin to 0
        total=0
        for key, value in quantities.items():
            #convert key stringg to int so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        
        return total
    
    def __len__(self):
        return len(self.cart)
    
    
    def get_prods(self):
        #get ids from cart
        product_ids=self.cart.keys()
        # use ids to lookup products in db model
        products = Product.objects.filter(id__in=product_ids)
        print("produts: son : " + str(products)) 
        #return our proucts
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self,product, quantity):
        product_id= str(product)
        product_qty= int(quantity)
        
        #  get cart
        ourcart = self.cart
        
        #update diccionary
        
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        
        
        # deal whith logged in user
        
        if self.request.user.is_authenticated:
            #get the curret user profile
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert to {'3':1} to {"3":1}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # Save our carty to the profile model
            
            current_user.update(old_cart=str(carty))
            
        thing = self.cart
        return thing
    
    def delete(self, product):
        
        product_id= str(product)
        #delete from diccionary / cart
        
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
        
        # deal whith logged in user
        
        if self.request.user.is_authenticated:
            #get the curret user profile
            
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # convert to {'3':1} to {"3":1}
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            # Save our carty to the profile model
            
            current_user.update(old_cart=str(carty))
        
        
            
            