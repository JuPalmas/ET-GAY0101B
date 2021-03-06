from django.views import generic
from web.models import Post
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import PostForm


def index(request):
    return render(request, 'web/index.html')

def crear_publicacion(request):

    data = {
        'form': PostForm()
    }
    if request.method == 'POST':
        formulario = PostForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Publicación creada con éxito"
        else:
            data["form"] = formulario
            data["mensaje"] = "Ha ocurrido un error en la creación"
    return render(request, "web/nueva_publicacion.html", data)

def register(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            usernames=formulario.cleaned_data["username"]
            messages.success(request,f"{usernames}")
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario
    return render(request,'registration/register.html',data)

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username' ,'first_name','last_name',"email","password1","password2"]


def listar_publicaciones(request):
    publicaciones = Post.objects.all()

    data = {
        'publicaciones' : publicaciones
    }
    return render(request, 'web/listar.html', data)
    

def modificar_publicacion(request,id):

    post = get_object_or_404(Post, id=id)
    data = {
        'form': PostForm(instance=post)
    }

    if request.method == 'POST':
        formulario = PostForm(data=request.POST, instance=post,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_publicaciones')
        data['form'] = formulario
    return render(request, 'web/editar_publicacion.html',data)

def eliminar_publicacion(request, id):

    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(to='listar_publicaciones')

class PostDetailView(generic.DetailView):
    model = Post