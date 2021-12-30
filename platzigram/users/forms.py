#Importaciones de Django
from django import forms

class ProfileForm(forms.Form):
    
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=11, required=True)
    profile_picture = forms.ImageField(required=False)