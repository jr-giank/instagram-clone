#Importaciones de Django
from django.db import models
from django.db.models.fields import EmailField, TextField

# Create your models here.

#Model usuarios
class User(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    is_admin = models.BooleanField(default=False)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name