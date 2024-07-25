from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.

#create customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    
# create user profile by default wher euse rsign in

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

#automate the profile thing


post_save.connect(create_profile, sender=User)    
    
    
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name
    #@daverobb2011
    class Meta:
        verbose_name_plural='categories'
        
        
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self) :
        return f'{self.first_name} {self.last_name}'
    

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=250, default='', blank=True, null=True)
    image=models.ImageField(upload_to='uploads/product/')
    #add sale stuff
    
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self) :
        return self.name
    

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100, default='', blank=True, null=True)
    phone=models.CharField(max_length=50, default='', blank=True, null=True)
    date= models.DateField(default=datetime.datetime.today)
    status= models.BooleanField(default=False)
    
    def __str__(self) :
        return self.product
    
    

class Charge(models.Model):
        nome_charge = models.CharField('Une Charge', max_length=120, null=True, blank=True)
        
        def __str__(self) -> str:
            return self.nome_charge

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # Obtener la extensión del archivo
    valid_extensions = ['.pdf', '.xls', '.xlsx', '.doc', '.docx','.jpg','.png']  # Extensiones permitidas
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de archivo no soportado. Sube archivos PDF, XLS, XLSX, DOC o DOCX.')

class FormulaireCharge(models.Model):
    date=models.DateTimeField('Date' , null=True, blank=True)
    charge=models.ForeignKey(Charge, blank=True, null=True, on_delete=models.CASCADE)
    prix = models.DecimalField('Prix', max_digits=10, decimal_places=2 , null=True, blank=True)  # Agregar max_digits y decimal_places
    #image_charge = models.ImageField(null=True, blank=True, upload_to="images/")
    image_charge = models.FileField('Fichier de charge', null=True, blank=True, upload_to="uploads/",
                                    validators=[validate_file_extension])
    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"FormulaireCharge Charge {self.charge} du {self.du} au {self.au} avec le montant {self.montant} "

class FormulaireArticle(models.Model):
    nom=models.CharField('Nom Article', max_length=120, blank=True, null=True)
    description = models.TextField('Description Article',max_length=15000, null=True, blank=True)
    prix = models.DecimalField('Prix', max_digits=10, decimal_places=2, null=True, blank=True)  # Agregar max_digits y decimal_places
    cree_le=models.DateTimeField('Cree le',default=datetime.datetime.today, null=True, blank=True)
    vendu= models.BooleanField('Vendu',default=False, null=True, blank=True)
    
    #image_charge = models.ImageField(null=True, blank=True, upload_to="images/")
    image_charge = models.FileField('Article chargé', null=True, blank=True, upload_to="uploads/",
                                    validators=[validate_file_extension])
    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"FormulaireArticle Nom Article {self.nom} date {self.cree_le} avec le montant {self.prix} "