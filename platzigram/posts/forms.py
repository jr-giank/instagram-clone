#Importaciones de Django 
from django import forms
from django.db.models import fields

#Models
from posts.models import Posts

class PostForm(forms.ModelForm):
    
    class Meta():

        model = Posts
        fields = ('user', 'profile', 'title', 'photo')