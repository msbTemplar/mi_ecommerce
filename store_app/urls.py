"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

#https://www.youtube.com/watch?v=CdtQSiC8ZNQ

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
    
    path('enregistrer_charge/', views.enregistrer_charge_view, name='enregistrer_charge'),
    path('liste_des_charges', views.liste_des_charges, name='liste_des_charges'),
    path('actualiser_la_charge/<id_charge>', views.actualiser_la_charge, name='actualiser_la_charge'),
    path('eliminer_la_charge/<id_charge>', views.eliminer_la_charge, name='eliminer_la_charge'),
    path('liste_des_formulaire_charges', views.liste_des_formulaire_charges, name='liste_des_formulaire_charges'),
    path('enregistrer_formulaire_charge/', views.enregistrer_formulaire_charge_view, name='enregistrer_formulaire_charge'),
    path('actualiser_formulaire_charge/<id_formulaire_charge>', views.actualiser_formulaire_charge, name='actualiser_formulaire_charge'),
    path('eliminer_formulaire_charge/<id_formulaire_charge>', views.eliminer_formulaire_charge, name='eliminer_formulaire_charge'),
    
     path('liste_des_formulaire_articles', views.liste_des_formulaire_articles, name='liste_des_formulaire_articles'),
    path('enregistrer_formulaire_article/', views.enregistrer_formulaire_article_view, name='enregistrer_formulaire_article'),
    path('actualiser_formulaire_article/<id_formulaire_article>', views.actualiser_formulaire_article, name='actualiser_formulaire_article'),
    path('eliminer_formulaire_article/<id_formulaire_article>', views.eliminer_formulaire_article, name='eliminer_formulaire_article'),
    
    path('liste_situation_caisse', views.liste_situation_caisse, name='liste_situation_caisse'),
    
    path('enregistrer_category/', views.enregistrer_category_view, name='enregistrer_category'),
    path('liste_des_categories', views.liste_des_categories, name='liste_des_categories'),
    path('actualiser_la_category/<id_category>', views.actualiser_la_category, name='actualiser_la_category'),
    path('eliminer_la_category/<id_category>', views.eliminer_la_category, name='eliminer_la_category'),


]

