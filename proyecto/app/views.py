from django.shortcuts import render

from app.models import *
from app.forms import UserRegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def index(request):
    return render(request, 'index.html')

def registrar(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")

            form.save()

            return render(request, 'index.html',{"mensaje": f"Se dio de alta {username}"})

    form = UserRegistrationForm(request.POST)
    return render (request, "registro.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"})
            else:
                return render(request, 'index.html', {"mensaje": "Usuario o contraseña invalidos"})
            
        else:
            return render (request,"index.html", {"mensaje": "Datos form incorrectos"})

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

