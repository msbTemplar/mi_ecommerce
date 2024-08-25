from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

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
    name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self) :
        return self.name
    #@daverobb2011
    class Meta:
        verbose_name_plural='categories'

class About(models.Model):
    description = models.TextField(null=True, blank=True)  # Cambiado a TextField para textos más largos
    
    def __str__(self):
        return self.description[:50]  # Devuelve los primeros 50 caracteres para una vista previa
    
    class Meta:
        verbose_name_plural = 'about'  # Cambiado a 'about' para que sea más representativo 
        
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
    quantite_product=models.IntegerField('Qantité article' , null=True, blank=True,default=0)
    
    # formulaire_article = models.ForeignKey('FormulaireArticle', on_delete=models.CASCADE, related_name='product', null=True)
    
    # @property
    # def quantite_product(self):
    #     return self.formulaire_article.quantite_article
    
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
    valid_extensions = ['.pdf', '.xls', '.xlsx', '.doc', '.docx','.jpg','.png','.jpeg','.txt','.xml']  # Extensiones permitidas
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de archivo no soportado. Sube archivos PDF, XLS, XLSX, DOC o DOCX.')

class FormulaireCharge(models.Model):
    date=models.DateTimeField('Date' , null=True, blank=True)
    charge=models.ForeignKey(Charge, blank=True, null=True, on_delete=models.CASCADE)
    description_charge = models.TextField('Description Charge',max_length=15000, null=True, blank=True)
    prix = models.DecimalField('Prix', max_digits=10, decimal_places=2 , null=True, blank=True)  # Agregar max_digits y decimal_places
    #image_charge = models.ImageField(null=True, blank=True, upload_to="images/")
    image_charge = models.FileField('Fichier de charge', null=True, blank=True, upload_to="uploads/",
                                    validators=[validate_file_extension])
    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"FormulaireCharge Charge {self.charge} date {self.date} avec le montant {self.prix} "

class FormulaireArticle(models.Model):
    ref_article = models.CharField('Référence Article', max_length=50, editable=True, unique=True, blank=True)
    quantite_article=models.IntegerField('Quantité Disponible des Article', default=0)
    nom=models.CharField('Nom Article', max_length=120, blank=True, null=True)
    description = models.TextField('Description Article',max_length=15000, null=True, blank=True)
    cout_revient_ozaz = models.DecimalField('Coût revient Ozaz', max_digits=10, decimal_places=2, null=True, blank=True)
    cout_revient_maallem = models.DecimalField('Coût revient Maallem', max_digits=10, decimal_places=2, null=True, blank=True)
    cout_revient_total = models.DecimalField('Coût revient Total', max_digits=10, decimal_places=2, null=True, blank=True)
    prix = models.DecimalField('Prix Estimé', max_digits=10, decimal_places=2, null=True, blank=True)  # Agregar max_digits y decimal_places
    cree_le=models.DateTimeField('Cree le',default=datetime.datetime.today, null=True, blank=True)
    vendu= models.BooleanField('Vendu',default=False, null=True, blank=True, editable=False)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1 , null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  null=False, blank=False)
    
    #image_charge = models.ImageField(null=True, blank=True, upload_to="images/")
    image_charge = models.FileField('Article chargé', null=True, blank=True, upload_to="uploads/",
                                    validators=[validate_file_extension])
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # Crear un nuevo artículo
            super(FormulaireArticle, self).save(*args, **kwargs)
            self.ref_article = f"OZ{self.pk:03d}"
            super(FormulaireArticle, self).save(*args, **kwargs)
        else:
            # Editar un artículo existente
            super(FormulaireArticle, self).save(*args, **kwargs)
    
    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"Ref Article: {self.ref_article} Nom Article: {self.nom} Quantite Article: {str(self.quantite_article)} "
    


"""
        if default_category is not None:
            default_category = default_category
        else:
            default_category = Category.objects.get(id=1)
        """
    
@receiver(post_save, sender=FormulaireArticle)
def create_product(sender, instance, created, **kwargs):
    print(f"Signal triggered for FormulaireArticle: {instance}")  # Verifica si la señal se activa

    if created:
        try:
            # Verificar si instance.category está presente y es válida
            if instance.category:
                category_instance = instance.category  # Obtener la instancia de la categoría
                print(f"Category associated with FormulaireArticle: {category_instance.name}")  # Depuración
            else:
                raise ValueError("No se ha asignado una categoría válida a FormulaireArticle.")

            # Crear el Product usando la instancia de la categoría del FormulaireArticle
            Product.objects.create(
                name=instance.nom,  # Map nom to name
                price=instance.prix,  # Map prix to price
                category=category_instance,  # Pasar la instancia de la categoría
                description=instance.description,  # Map description to description
                image=instance.image_charge,  # Map image_charge to image
                is_sale=instance.vendu,  # Map vendu to is_sale
                sale_price=instance.prix if instance.vendu else 0,  # Set sale_price if vendu is True
                quantite_product=instance.quantite_article
            )
            print("Product created successfully.")  # Depuración

        except Exception as e:
            print(f"Error creating product: {str(e)}")  # Depuración

@receiver(post_save, sender=FormulaireArticle)
def update_product(sender, instance, **kwargs):
    if hasattr(instance, 'quantite_article') :
        try:
            product = Product.objects.get(name=instance.nom)
            product.quantite_product = instance.quantite_article
            product.save()
            print(f"Product updated with new quantity: {instance.quantite_article}")
        except Product.DoesNotExist:
            print(f"Product with name {instance.nom} does not exist.")
        except Exception as e:
            print(f"Error updating product: {str(e)}")
    
    if hasattr(instance, 'prix') :
        try:
            product = Product.objects.get(name=instance.nom)
            product.price = instance.prix
            product.save()
            print(f"Product updated with new quantity: {instance.prix}")
        except Product.DoesNotExist:
            print(f"Product with prix {instance.prix} does not exist.")
        except Exception as e:
            print(f"Error updating product: {str(e)}")
    
    if hasattr(instance, 'category') :
        try:
            product = Product.objects.get(name=instance.nom)
            product.category = instance.category
            product.save()
            print(f"Product updated with new category: {instance.category}")
        except Product.DoesNotExist:
            print(f"Product with category {instance.category} does not exist.")
        except Exception as e:
            print(f"Error updating product: {str(e)}")
    
    if hasattr(instance, 'description') :
        try:
            product = Product.objects.get(name=instance.nom)
            product.description = instance.description
            product.save()
            print(f"Product updated with new description: {instance.description}")
        except Product.DoesNotExist:
            print(f"Product with description {instance.description} does not exist.")
        except Exception as e:
            print(f"Error updating product: {str(e)}")
    
    if hasattr(instance, 'category') :
        try:
            print(f"Attempting to update product with category: {instance.category}")
            

            product = Product.objects.get(category=instance.category)
            print(f"Current product name: {product.name}")
            product.name = instance.nom
            product.save()
            print(f"Product updated with new nom: {instance.nom}")
        except Product.DoesNotExist:
            print(f"Product with nom {instance.nom} does not exist.")
        except Exception as e:
            print(f"Error updating product: {str(e)}")
 
def get_category_for_article(article):
    # Aquí defines tu lógica para seleccionar la categoría
    # Por ejemplo, basado en el nombre del artículo:
    if "electronic" in article.nom.lower():
        return Category.objects.get(name="Programming Books")
    elif "clothing" in article.nom.lower():
        return Category.objects.get(name="Clothing")
    else:
        return Category.objects.get(name="General")  # Default category

@receiver(post_delete, sender=FormulaireArticle)
def delete_product(sender, instance, **kwargs):
    try:
        # Busca y elimina el Product relacionado con el FormulaireArticle eliminado
        Product.objects.filter(name=instance.nom, price=instance.prix).delete()
        print(f"Product associated with FormulaireArticle '{instance.nom}' deleted.")
    except Exception as e:
        print(f"Error deleting product: {str(e)}")


class FormulaireClient(models.Model):
    nom=models.CharField('Nom', max_length=120, blank=True, null=True)
    prenom=models.CharField('Prenom', max_length=120, blank=True, null=True)
    tel=models.CharField('Tel', max_length=120, blank=True, null=True)
    email=models.CharField('Email', max_length=120, blank=True, null=True)
    addresse = models.TextField('Addresse',max_length=15000, null=True, blank=True)
    description = models.TextField('Description',max_length=15000, null=True, blank=True)
    cree_le=models.DateTimeField('Cree le',default=datetime.datetime.today, null=True, blank=True)
        
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"{self.nom}  {self.prenom} "

class FormulaireVente(models.Model):
    ETAT_VENTE_CHOICES = [
        ('Vendu', 'Vendu'),
        ('Commande', 'Commande')
    ]
    ETAT_LIVRER_CHOICES = [
        ('Livrer', 'Livrer'),
        ('En_instance_de_livraison', 'En instance de livraison')
    ]
    ETAT_PAYER_CHOICES = [
        ('Payer', 'Payer'),
        ('En_instance_de_payement', 'En instance de payement')
    ]
    ETAT_FINAL_CHOICES = [
        ('Cheque', 'Cheque'),
        ('Espece', 'Espece'),
        ('Virement', 'Virement')
    ]
    article_vente=models.ForeignKey(FormulaireArticle, blank=True, null=True, on_delete=models.CASCADE)
    quantite_vente = models.PositiveIntegerField('Quantité Vente', null=False, blank=False, default=0)  # Nuevo campo

    date_vente=models.DateTimeField('Date Vente' , null=True, blank=True)
    client_vente=models.ForeignKey(FormulaireClient, blank=True, null=True, on_delete=models.CASCADE)
    description_vente= models.TextField('Description Vente',max_length=15000, null=True, blank=True)
    category_vente = models.CharField('Category Vente', max_length=120, blank=True, null=True)
    cout_revient_total_vente = models.DecimalField('Coût revient Total Vente', max_digits=20, decimal_places=2, null=True, blank=True)
    prix_vente = models.DecimalField('Prix Estimé', max_digits=20, decimal_places=2 , null=True, blank=True)  # Agregar max_digits y decimal_places
    etat_vente=models.CharField('Etat Vente', max_length=120, blank=True, null=True, choices=ETAT_VENTE_CHOICES)
    etat_livrer=models.CharField('Etat Livraison', max_length=120, blank=True, null=True, choices=ETAT_LIVRER_CHOICES)
    etat_payer=models.CharField('Etat Payement', max_length=120, blank=True, null=True, choices=ETAT_PAYER_CHOICES)
    etat_final=models.CharField('Etat Final', max_length=120, blank=True, null=True, choices=ETAT_FINAL_CHOICES)
    #vendu_vente= models.BooleanField('Vendu',default=True)
    hidden_vendu_vente = models.BooleanField('Vente Vendu?', default=False)
    marge_pourcentage = models.DecimalField('Marge %', max_digits=10, decimal_places=2 , null=True, blank=True)  # Agregar max_digits y decimal_places
    marge_chifre = models.DecimalField('Marge En Chifre', max_digits=10, decimal_places=2 , null=True, blank=True)  # Agregar max_digits y decimal_places

    cree_le=models.DateTimeField('Cree le',default=datetime.datetime.today, null=True, blank=True)
    
    """def save(self, *args, **kwargs):
        # Verificar que el artículo tenga suficiente cantidad antes de procesar la venta
        if self.article_vente:
            # Verificar que la cantidad solicitada no sea mayor que la disponible
            if self.quantite_vente > self.article_vente.quantite_article:
                raise ValidationError("La quantité demandée dépasse la quantité disponible en stock.")

            # Disminuir la cantidad del artículo vendido
            self.article_vente.quantite_article -= self.quantite_vente
            self.article_vente.save()
            
        if self.prix_vente and self.cout_revient_total_vente:
            self.marge_chifre = self.prix_vente - self.cout_revient_total_vente
            # Calcular la marge_pourcentage
            self.marge_pourcentage = ((self.prix_vente - self.cout_revient_total_vente) / self.prix_vente) * 100
        super().save(*args, **kwargs) """
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Si no hay PK, es una nueva instancia
            if self.article_vente:
                # Verificar que la cantidad solicitada no sea mayor que la disponible
                if self.quantite_vente > self.article_vente.quantite_article:
                    raise ValidationError("La quantité demandée dépasse la quantité disponible en stock.")

                # Disminuir la cantidad del artículo vendido
                self.article_vente.quantite_article -= self.quantite_vente
                self.article_vente.save()

        else:  # Es una actualización
            # Obtener la instancia original para comparar cantidades
            original_instance = FormulaireVente.objects.get(pk=self.pk)
            if self.article_vente and self.quantite_vente != original_instance.quantite_vente:
                # Calcular la diferencia y ajustar el inventario
                difference = self.quantite_vente - original_instance.quantite_vente
                if difference > 0 and difference > self.article_vente.quantite_article:
                    raise ValidationError("La quantité demandée dépasse la quantité disponible en stock.")
                
                self.article_vente.quantite_article -= difference
                self.article_vente.save()

        # Calcular las margenes
        if self.prix_vente and self.cout_revient_total_vente:
            self.marge_chifre = self.prix_vente - self.cout_revient_total_vente
            self.marge_pourcentage = ((self.prix_vente - self.cout_revient_total_vente) / self.prix_vente) * 100
        
        super().save(*args, **kwargs)

    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"FormulaireVente  Article {self.article_vente} date vente {self.date_vente} avec le prix {self.prix_vente} "