from .cart import Cart

# create context processor so out cart can work on all pages 

def cart(request):
    #return the default data ffrom our cart
    context={'cart':Cart(request)}
    return context