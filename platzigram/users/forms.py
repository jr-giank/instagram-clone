#Importaciones de Django
from django import forms

from django.contrib.auth.models import User
from users.models import Profile
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    
    #Creacion de formulario de Signup
    #Se usa sttrs para hacer el bootstrap por ahi

    username = forms.CharField(
        label=False, 
        min_length=4, 
        max_length=50, 
        widget=forms.TextInput(
            attrs={
                'class':"form-control", 
                'placeholder':"Username", 
                'name':"username", 
                'required':"true"
            }
        )
    )
    password = forms.CharField(
        label=False,
        max_length=70, 
        widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password", 'name':"password", 'required':"true"})
    )
    password_confirmation = forms.CharField(
        label=False,
        max_length=70, 
        widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password Confirmation", 'name':"password_confirmation", 'required':"true"})
    )
    first_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50, 
        widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"First Name", 'name':"first_name", 'required':"true"})
    )
    last_name = forms.CharField(
        label=False,
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Last Name", 'name':"last_name", 'required':"true"})
    )
    email = forms.CharField(
        label=False,
        min_length=6, 
        max_length=70, 
        widget=forms.EmailInput(attrs={'class':"form-control", 'placeholder':"Email", 'name':"email", 'required':"true"})
    )

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken == True:
            raise forms.ValidationError('Username is already in use')
        
        return username

    def clean(self):

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password does not match')

        return data

    def save(self):
        """create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')#Sirve para sacar ese dato de la lista, ya que no lo necesitamos en el formulario

        user = User.objects.create_user(**data)
        profile = Profile(user= user)
        profile.save()

class ProfileForm(forms.Form):
    
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=11, required=True)
    profile_picture = forms.ImageField(required=False)