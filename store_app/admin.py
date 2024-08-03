from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Profile)
admin.site.register(models.Charge)
admin.site.register(models.FormulaireArticle)
admin.site.register(models.FormulaireCharge)
#About
admin.site.register(models.About)
# mist profile info and user info

class ProfileInline(admin.StackedInline):
    model = models.Profile
    

#extand user model

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name","last_name", "email"]
    inlines=[ProfileInline]
    
    

#Unregester the old way

admin.site.unregister(User)

#re register the new way
admin.site.register(User, UserAdmin)