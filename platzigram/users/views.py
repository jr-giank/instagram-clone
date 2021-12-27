#Importaciones de Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

#Modelos 
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Username or Password incorret'})
    
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)

    return redirect('login')

def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user =  User.objects.create_user(username = username, password = password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email'] 

        profile = Profile(user=user)

        user.save()
        profile.save()
        return redirect('login')

    return render(request, 'users/signup.html')