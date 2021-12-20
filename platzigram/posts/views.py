"""Posts Views"""

#Importaciones de Django
from django.shortcuts import render
from django.http import HttpResponse

#Utilities
from datetime import datetime as dt

#Globales
posts_list_dictionaries = [
    {
        'name': 'Gianfranco De Paula',
        'user': 'jr.gian_k',
        'timestamp': dt.now().strftime('%d/%m/%Y, %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200',
    },

    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': dt.now().strftime('%d/%m/%Y, %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },

    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': dt.now().strftime('%d/%m/%Y, %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
]

# Create your views here.
def list_post(request):
    
    const = []

    for post in posts_list_dictionaries:
        const.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src = "{picture}"></figure>
        """.format(**post))

    return HttpResponse("<br>".join(const))