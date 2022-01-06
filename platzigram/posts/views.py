"""Posts Views"""

#Importaciones de Django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

#Models
from posts.models import Posts

#Importaciones del form de Django
from posts.forms import PostForm

# Create your views here.
@login_required #Sirve para que si no se a autentificado un usuario pues no se pueda acceder a posts, hay que configurar LOGIN_URL = /login/ en settings
def list_post(request):

    post = Posts.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', {'posts': post})

@login_required
def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'posts/new.html', {'form': form, 'user': request.user, 'profile': request.user.profile})