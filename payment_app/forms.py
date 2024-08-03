from django import forms 
from .models import ShippingAddress

# phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone'}), required=False)

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nom Complet'}), required=False)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email'}), required=False)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Addresse'}), required=False)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Téléphone'}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ville'}), required=False)
    shipping_state= forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Commune'}), required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Code Postal'}), required=False)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Pays'}), required=False)
    
    class Meta:
        model = ShippingAddress
        fields=['shipping_full_name', 'shipping_email', 'shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_zipcode','shipping_country']
        
        exclude=['user',]
        
    
class PaymentForm(forms.Form):
    card_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Card Name'}), required=False)
    card_number=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Card Number'}), required=False)
    card_exp_date=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Exp Date'}), required=False)
    card_cvv_number=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Cvv Number'}), required=False)
    card_address1=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Address 1'}), required=False)
    card_address2=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Address 2'}), required=False)
    card_city=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing City'}), required=False)
    card_state=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing State'}), required=False)
    card_zipcode=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing ZipCode'}), required=False)
    card_country=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Country'}), required=False)