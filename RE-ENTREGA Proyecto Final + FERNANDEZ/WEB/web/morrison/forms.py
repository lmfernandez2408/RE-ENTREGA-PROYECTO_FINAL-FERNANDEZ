from django import forms 
from .models import Mapa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = '__all__'

class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña Antigua', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña Antigua', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}  

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


