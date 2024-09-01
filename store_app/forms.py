from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile,Charge,FormulaireCharge,FormulaireArticle,Category,About,FormulaireClient,FormulaireVente


class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone'}), required=False)
    address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address 1'}), required=False)
    address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address 2'}), required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'City'}), required=False)
    state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'State'}), required=False)
    zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zip Code'}), required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Country'}), required=False)
    
    class Meta:
        model = Profile
        fields = ['phone', 'address1','address2','city','state','zipcode','country',]
    

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
        
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        
                
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    

class UpdateUserForm(UserChangeForm):
    #hide password stuff
    password = None
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),required=False)
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),required=False)
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        
		
    


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class EnregistrerChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = '__all__'
        widgets = {'nome_charge': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire la charge','name':'nome_charge'}),}

class EnregistrerFormulaireChargeForm(forms.ModelForm):
    class Meta:
        model = FormulaireCharge
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date', 'type': 'date'}),
            'charge': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Charge'}),
            'description_charge': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Description Charge'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant', 'id': 'id_montant', 'min': '0', 'step': '0.01'}),
            'image_charge': forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'files', 'id': 'formFile'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener las opciones dinámicamente desde el modelo Charge
        self.fields['charge'].queryset = Charge.objects.all()  # Puedes ajustar esto según tus necesidades de filtrado
        

class EnregistrerFormulaireArticleForm(forms.ModelForm):
    class Meta:
        model = FormulaireArticle
        fields = '__all__'
        widgets = {
            'ref_article': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_article'}),
            'quantite_article': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantite Article', 'id': 'id_quantite_article', 'min': '0', 'step': '1', 'name' : 'quantite_article'}),
            
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire le nom','name':'nom'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Description Article' , 'id': 'id_description', 'name':'description'}),
            'cout_revient_ozaz': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coût revient Ozaz', 'id': 'id_cout_revient_ozaz', 'min': '0', 'step': '0.01'}),
            'cout_revient_maallem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coût revient Maallem', 'id': 'id_cout_revient_maallem', 'min': '0', 'step': '0.01'}),
            'cout_revient_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coût revient Total', 'id': 'id_cout_revient_total', 'min': '0', 'step': '0.01' , 'readonly': 'readonly', 'name':'cout_revient_total'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix', 'id': 'id_prix', 'min': '0', 'step': '0.01' , 'id': 'id_prix', 'name':'prix'}),
            'cree_le': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Cree le', 'type': 'date'}),
            'vendu': forms.CheckboxInput(attrs={'class': 'form-check-input', 'hidden':'hidden'}),
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Category', 'required': True, 'name': 'category', 'id': 'id_category'}),
            'image_charge': forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'files', 'id': 'formFile'}),
        }
    def __init__(self, *args, **kwargs):
        super(EnregistrerFormulaireArticleForm, self).__init__(*args, **kwargs)
        print(self.fields.keys())
        if 'ref_article' in self.fields:
            self.fields['ref_article'].widget.attrs['readonly'] = True
            self.fields['ref_article'].widget.attrs['class'] = 'form-control'
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener el último valor de codeFormCotiz de la base de datos
        last_code = FormulaireArticle.objects.order_by('-id').first()
        if last_code and last_code.id is not None:
            next_code = f"OZ{(last_code.id + 1):03d}"
        else:
            #next_code = 2205
            next_code = f"OZ{(0 + 1):03d}"
        self.fields['ref_article'].initial = next_code
    
    

class EnregistrerCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire la charge','name':'name_category'}),}
        

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['description']  # Incluye los campos que deseas mostrar en el formulario
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Introducir la descripción',
                'rows': 4,  # Ajusta el número de filas según sea necesario
            }),}

class EnregistrerFormulaireClientForm(forms.ModelForm):
    class Meta:
        model = FormulaireClient
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire le nom','name':'nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire le prenom','name':'prenom'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire le telephone','name':'tel'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire le email','name':'email'}),
            'addresse': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Introduire addresse'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Introduire Description'}),
            'cree_le': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Cree le', 'type': 'date'}),
            
        }


class EnregistrerFormulaireVenteForm(forms.ModelForm):
    class Meta:
        model = FormulaireVente
        fields = '__all__'
        widgets = {
            'article_vente': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Article', 'required': True, 'name': 'article', 'id':'id_article'}),
            'quantite_vente': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Qauntité Vente Article', 'id': 'id_quantite_vente', 'min': '0','name': 'quantite_vente'}),

            'date_vente': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Vente', 'type': 'date', 'id': 'id_date_vente'}),
            'client_vente':forms.Select(attrs={'class': 'form-select', 'placeholder': 'Client Vente', 'required': True, 'name': 'client_vente', 'id':'id_client_vente'}),
            'description_vente': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Description Vente', 'name':'description', 'id':'id_description'}),
            'category_vente': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Categorie Vente', 'name':'category', 'id':'id_category'}),

            'cout_revient_total_vente': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coût revient Total Vente', 'id': 'id_cout_revient_total_vente', 'min': '0', 'step': '0.01' , 'readonly': 'readonly'}),
            'prix_vente': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix', 'id': 'id_prix', 'name':'prix', 'min': '0', 'step': '0.01'}),
            'etat_vente': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Etat Vente', 'required': False, 'name': 'etat_vente', 'id':'id_etat_vente'}, choices=FormulaireVente.ETAT_VENTE_CHOICES),
            'etat_livrer': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Etat Livraison', 'required': False, 'name': 'etat_livrer', 'id':'id_etat_livrer'}, choices=FormulaireVente.ETAT_LIVRER_CHOICES),
            'etat_payer': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Etat Livraison', 'required': False, 'name': 'etat_payer', 'id':'id_etat_payer'}, choices=FormulaireVente.ETAT_PAYER_CHOICES),
            'etat_final': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Etat Final', 'required': False, 'name': 'etat_final', 'id':'id_etat_final'}, choices=FormulaireVente.ETAT_FINAL_CHOICES),
            #'vendu_vente': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':'id_vendu_vente', 'name': 'vendu_vente'}),
            'hidden_vendu_vente': forms.CheckboxInput(attrs={'class': 'form-check-input','id':'id_hidden_vendu_vente'}),
            'marge_pourcentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Marge Pourcentage', 'id': 'id_marge_pourcentage', 'name':'marge_pourcentage', 'min': '0', 'step': '0.01','readonly': 'readonly'}),
            'marge_chifre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Marge Chifre', 'id': 'id_marge_chifre', 'name':'marge_chifre', 'min': '0', 'step': '0.01', 'readonly': 'readonly'}),

            
            
            'cree_le': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Cree le', 'type': 'date'}),

        }
    def clean_quantite_vente(self):
        quantite_vente = self.cleaned_data.get('quantite_vente')
        article_vente = self.cleaned_data.get('article_vente')

        if article_vente and quantite_vente > self.cleaned_data.get('article_vente').quantite_article:
            raise forms.ValidationError(f"La quantité demandée ({quantite_vente}) dépasse la quantité disponible en stock ({self.cleaned_data.get('article_vente').quantite_article}).")

        return quantite_vente
    
    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.errors.get('quantite_vente'):
            self.fields['quantite_vente'].widget.attrs.update({'class': 'is-invalid'}) """
   
                                    
    def is_valid(self):
        valid = super().is_valid()
        if valid:
            quantite_vente = self.cleaned_data.get('quantite_vente')
            article_vente = self.cleaned_data.get('article_vente')
            #vendu_vente = self.cleaned_data.get('vendu_vente', False)

            
            if article_vente and quantite_vente > self.cleaned_data.get('article_vente').quantite_article:
                return False
        return valid
    
    """ # Esto es en el formulario ModelForm, en el método is_valid o en la vista:
    def save(self, *args, **kwargs):
        vendu_vente = self.cleaned_data.get('vendu_vente', False)
        # 'vendu_vente' ya contendrá True o False basado en el checkbox
        super().save(*args, **kwargs) """
    
    """ def clean(self):
            cleaned_data = super().clean()
            vendu_vente = cleaned_data.get("vendu_vente")
        
        
            return cleaned_data """
    
    def save(self, commit=True):
        article_vente = self.cleaned_data.get('article_vente')
        quantite_vente = self.cleaned_data.get('quantite_vente')

        # Verifica si el formulario se está creando o actualizando
        if self.instance.pk is None:
            # Es una nueva instancia, descontar la cantidad
            # article_vente.quantite_article -= quantite_vente
            # article_vente.save()
            pass
        else:
            # Es una actualización, manejar el caso aquí
            original_instance = FormulaireVente.objects.get(pk=self.instance.pk)
            quantite_vente_originale = original_instance.quantite_vente

            # Si la cantidad cambió, ajusta el inventario
            if quantite_vente != quantite_vente_originale:
                # difference = quantite_vente - quantite_vente_originale
                # article_vente.quantite_article -= difference
                # article_vente.save()
                pass

        return super().save(commit=commit)