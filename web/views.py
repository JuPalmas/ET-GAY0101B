from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

def index(request):
    return render(request, 'web/index.html', {})

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

def publicar(request):
    return render(request, 'web/nueva_publicacion.html', {})

    