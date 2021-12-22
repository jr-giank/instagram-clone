#Importaciones de  Django
from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import OneToOneField 

# Create your models here.
class Profile(models.Model):
    """
    - Profile Model
    - Proxy que extiende de la data base con otra información
    """
    
    user = models.OneToOneField(User, on_delete=CASCADE)
    
    website = models.URLField(max_length=200, blank=True)
    biography = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    profile_picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username
