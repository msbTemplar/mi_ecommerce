from django.db import models
from django.contrib.auth.models import User
from store_app.models import Product
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime

# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255, null=True, blank=True)
    shipping_email = models.CharField(max_length=255, null=True, blank=True)
    shipping_address1 = models.CharField(max_length=255, null=True, blank=True)
    shipping_address2 = models.CharField(max_length=255, null=True, blank=True)
    shipping_city = models.CharField(max_length=255, null=True, blank=True)
    shipping_state = models.CharField(max_length=255, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=255, null=True, blank=True)
    shipping_country = models.CharField(max_length=255, null=True, blank=True)
    
    #dont pluriez address
    
    class Meta:
        verbose_name_plural = "Shipping Address"
        
    
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'
    

# create shipping address by default wher euse rsign in

def create_shipping(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

#automate the profile thing


post_save.connect(create_shipping, sender=User)    
    

#create order model

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    shipping_address = models.TextField(max_length=15000, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped=models.BooleanField(default=False, null=True, blank=True)
    date_shipped=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'Order - {str(self.id)}'

#auto add shipping dte
@receiver(pre_save, sender=Order)

def set_shipped_date_on_update(sender, instance, **kwargs):
    if instance.pk:
        now = datetime.datetime.now()
        obj = sender._default_manager.get(pk=instance.pk)
        if instance.shipped and not obj.shipped:
            instance.date_shipped= now
            
    

# create order item model

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    
    quantity = models.PositiveBigIntegerField(default=1, null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f'Order Item - {str(self.id)}'