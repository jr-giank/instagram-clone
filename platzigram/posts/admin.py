#Importaciones de Django
from django.contrib import admin

#Importaciones locales
from posts.models import Posts

# Register your models here.
@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_filter = (
                'created',
                'modified'
    )