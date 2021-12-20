import json
from django.http import HttpResponse
import datetime
from django.http import response
import json

from django.http.response import JsonResponse

def home(request):
    
    return HttpResponse("Hello World")

def hora_actual(request):

    hora_fecha = datetime.datetime.now().strftime('%H:%M')

    return HttpResponse("La hora del servidos es: " + str(hora_fecha))

def sorted_integers(request):
    
    numbers = sorted(request.GET['numbers'].split(','))
    return HttpResponse(str(numbers), content_type='application/json')

def bienvenida(request, name, age):

    if age <= 15:
        message = f"sorry you can't be here {name}"
    else:
        message = f"Welcome to platzigram {name}"

    return HttpResponse(message)
