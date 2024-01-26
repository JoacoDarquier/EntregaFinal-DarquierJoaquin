from django.shortcuts import render

from app.models import *
from app.forms import UserRegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

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

#CRUD Arquero
class ArqueroList (ListView):
    model = Arquero
    template_name = 'arqueros_list.html'

class ArqueroCreacion (CreateView):
    model = Arquero
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'create_arquero.html'
    success_url = "/yo-jugador/arquero/list"

class ArqueroDetalle (DetailView):
    model = Arquero
    template_name = 'arquero_detalle.html'

class ArqueroDelete (DeleteView):
    model = Arquero
    template_name = 'arquero_confirm_delete.html'

class ArqueroEditar (UpdateView):
    model = Arquero
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'arquero_editar.html'
    success_url = "/app/arquero/list"


#CRUD Defensor
class DefensorList (ListView):
    model = Defensor
    template_name = 'defensores_list.html'

class DefensorCreacion (CreateView):
    model = Defensor
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'defensor_create.html'
    success_url = "/yo-jugador/defensor/list"

class DefensorDetalle (DetailView):
    model = Defensor
    template_name = 'defensor_detalle.html'

class DefensorDelete (DeleteView):
    model = Defensor
    template_name = 'defensor_confirm_delete.html'

class DefensorEditar (UpdateView):
    model = Defensor
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'defensor_editar.html'
    success_url = "/yo-jugador/defensor/list"


#CRUD Mediocampista
class MediocampistaList (ListView):
    model = Mediocampista
    template_name = 'mediocampistas_list.html'

class MediocampistaCreacion (CreateView):
    model = Mediocampista
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'mediocampista_create.html'
    success_url = "/yo-jugador/mediocampista/list"

class MediocampistaDetalle (DetailView):
    model = Mediocampista
    template_name = 'mediocampista_detalle.html'

class MediocampistaDelete (DeleteView):
    model = Mediocampista
    template_name = 'mediocampista_confirm_delete.html'

class MediocampistaEditar (UpdateView):
    model = Mediocampista
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'mediocampista_editar.html'
    success_url = "/yo-jugador/mediocampista/list"


#CRUD Delantero
class DelanteroList (ListView):
    model = Delantero
    template_name = 'delanteros_list.html'

class DelanteroCreacion (CreateView):
    model = Delantero
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'delantero_create.html'
    success_url = "/yo-jugador/delantero/list"

class DelanteroDetalle (DetailView):
    model = Delantero
    template_name = 'delantero_detalle.html'

class DelanteroDelete (DeleteView):
    model = Delantero
    template_name = 'delantero_confirm_delete.html'

class DelanteroEditar (UpdateView):
    model = Delantero
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'delantero_editar.html'
    success_url = "/yo-jugador/delantero/list"

