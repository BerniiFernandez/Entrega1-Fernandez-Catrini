from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class NetflixForm(forms.Form):
    title = forms.CharField(max_length=100)
    photo = forms.ImageField(label="Photo")
    date = forms.DateField()
    author = forms.CharField(max_length=50)
    qualification = forms.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()

class PrimeForm(forms.Form):
    title = forms.CharField(max_length=100)
    photo = forms.ImageField(label="Photo")
    date = forms.DateField()
    author = forms.CharField(max_length=50)
    qualification = forms.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()
    
class HBOForm(forms.Form):
    title = forms.CharField(max_length=100)
    photo = forms.ImageField(label="Photo")
    date = forms.DateField()
    author = forms.CharField(max_length=50)
    qualification = forms.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()

class DisneyForm(forms.Form):
    title = forms.CharField(max_length=100)
    photo = forms.ImageField(label="Photo")
    date = forms.DateField()
    author = forms.CharField(max_length=50)
    qualification = forms.DecimalField(max_digits=2, decimal_places=1)
    body = RichTextField()



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    link = forms.URLField()
    photo = forms.ImageField(label="Photo")
    password1= forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'link', 'photo', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    first_name=forms.CharField(label='Modificar nombre')
    last_name=forms.CharField(label='Modificar apellido')
    email = forms.EmailField()
    link = forms.URLField()
    photo = forms.ImageField(label="Photo")
    password1= forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'link', 'photo', 'password1', 'password2',]
        help_texts = {k:"" for k in fields}    
