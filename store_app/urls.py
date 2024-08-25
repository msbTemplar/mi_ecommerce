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
    path('about/<int:pk>/', views.create_or_update_about, name='update_about'),
    path('about/new/', views.create_or_update_about, name='create_about'),
    path('liste_about', views.liste_about, name='liste_about'),
    path('actualiser_about/<id_about>', views.actualiser_about, name='actualiser_about'),
    path('eliminer_about/<id_about>', views.eliminer_about, name='eliminer_about'),
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
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
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
    path('liste_des_formulaire_clients', views.liste_des_formulaire_clients, name='liste_des_formulaire_clients'),
    path('enregistrer_formulaire_client/', views.enregistrer_formulaire_client_view, name='enregistrer_formulaire_client'),
    path('actualiser_formulaire_client/<id_formulaire_client>', views.actualiser_formulaire_client, name='actualiser_formulaire_client'),
    path('eliminer_formulaire_client/<id_formulaire_client>', views.eliminer_formulaire_client, name='eliminer_formulaire_client'),
    path('liste_des_formulaire_ventes', views.liste_des_formulaire_ventes, name='liste_des_formulaire_ventes'),
    path('enregistrer_formulaire_vente/', views.enregistrer_formulaire_vente_view, name='enregistrer_formulaire_vente'),
    path('actualiser_formulaire_vente/<id_formulaire_vente>', views.actualiser_formulaire_vente, name='actualiser_formulaire_vente'),
    path('eliminer_formulaire_vente/<id_formulaire_vente>', views.eliminer_formulaire_vente, name='eliminer_formulaire_vente'),
    path('get_article_data/<int:pk>/', views.get_article_data, name='get_article_data'),
    path('get_last_id/', views.get_last_id, name='get_last_id'),

]

