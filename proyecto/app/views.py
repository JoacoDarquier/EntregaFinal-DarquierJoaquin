from django.shortcuts import render, redirect

from app.models import Arquero, Defensor, Mediocampista, Delantero, Avatar 

from app.forms import UserRegistrationForm, AvatarFormulario, ArqueroFormulario

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.exceptions import PermissionDenied



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

def login_request(request):
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
class ArqueroList (LoginRequiredMixin, ListView):
    model = Arquero
    template_name = 'arqueros_list.html'

class ArqueroCreacion (LoginRequiredMixin, CreateView):
    model = Arquero
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'create_arquero.html'
    success_url = "/yo-jugador/arquero/list"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

'''def arquero_create(request):
    if request.method == 'POST':
        form = ArqueroFormulario(request.POST, request.FILES)
        if form.is_valid():
            arquero = form.save(commit=False)
            arquero.usuario = request.user
            arquero.save()
            return redirect('index')
    else:
        form = ArqueroFormulario()
    return render(request, 'create_arquero.html', {'form': form})'''

class ArqueroDetalle (LoginRequiredMixin, DetailView):
    model = Arquero
    template_name = 'arquero_detalle.html'

class ArqueroDelete (LoginRequiredMixin, DeleteView):
    model = Arquero
    template_name = 'arquero_confirm_delete.html'
    success_url = "/yo-jugador/arquero/list"

class ArqueroEditar (LoginRequiredMixin, UpdateView):
    model = Arquero
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'arquero_editar.html'
    success_url = "/yo-jugador/arquero/list"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied("No tienes permiso para editar este objeto.")
        return obj


#CRUD Defensor
class DefensorList (LoginRequiredMixin, ListView):
    model = Defensor
    template_name = 'defensores_list.html'

class DefensorCreacion (LoginRequiredMixin, CreateView):
    model = Defensor
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'defensor_create.html'
    success_url = "/yo-jugador/defensor/list"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class DefensorDetalle (LoginRequiredMixin, DetailView):
    model = Defensor
    template_name = 'defensor_detalle.html'

class DefensorDelete (LoginRequiredMixin, DeleteView):
    model = Defensor
    template_name = 'defensor_confirm_delete.html'

class DefensorEditar (LoginRequiredMixin, UpdateView):
    model = Defensor
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'defensor_editar.html'
    success_url = "/yo-jugador/defensor/list"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied("No tienes permiso para editar este objeto.")
        return obj


#CRUD Mediocampista
class MediocampistaList (LoginRequiredMixin, ListView):
    model = Mediocampista
    template_name = 'mediocampistas_list.html'

class MediocampistaCreacion (LoginRequiredMixin, CreateView):
    model = Mediocampista
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'mediocampista_create.html'
    success_url = "/yo-jugador/mediocampista/list"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class MediocampistaDetalle (LoginRequiredMixin, DetailView):
    model = Mediocampista
    template_name = 'mediocampista_detalle.html'

class MediocampistaDelete (LoginRequiredMixin, DeleteView):
    model = Mediocampista
    template_name = 'mediocampista_confirm_delete.html'

class MediocampistaEditar (LoginRequiredMixin, UpdateView):
    model = Mediocampista
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'mediocampista_editar.html'
    success_url = "/yo-jugador/mediocampista/list"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied("No tienes permiso para editar este objeto.")
        return obj


#CRUD Delantero
class DelanteroList (LoginRequiredMixin, ListView):
    model = Delantero
    template_name = 'delanteros_list.html'

class DelanteroCreacion (LoginRequiredMixin, CreateView):
    model = Delantero
    fields = ['nombre', 'apellido', 'pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email', 'fecha_nacimiento']
    template_name = 'delantero_create.html'
    success_url = "/yo-jugador/delantero/list"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class DelanteroDetalle (LoginRequiredMixin, DetailView):
    model = Delantero
    template_name = 'delantero_detalle.html'

class DelanteroDelete (LoginRequiredMixin, DeleteView):
    model = Delantero
    template_name = 'delantero_confirm_delete.html'

class DelanteroEditar (LoginRequiredMixin, UpdateView):
    model = Delantero
    fields = ['pie_habil', 'cant_clubes_anteriores', 'telefono', 'estatura', 'email',]
    template_name = 'delantero_editar.html'
    success_url = "/yo-jugador/delantero/list"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.usuario != self.request.user:
            raise PermissionDenied("No tienes permiso para editar este objeto.")
        return obj


'''@login_required
def avatar (request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            user = User.objects.get(username=request.user)
            avatar = Avatar(user=user,image=formulario.cleaned_data.get("image"))
            avatar.save()
            return render(request, 'index.html')
    formulario = AvatarFormulario()

    return render (request, 'usuario_avatar.html', {'formulario' : formulario})'''


def avatar(request):
    if request.method == "POST":
        print("avatar - POST")
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            print("avatar - Is_Valid!")
            user = request.user
            avatar = Avatar.objects.filter(user=user).first()
            if avatar:
                avatar.delete()
            avatar = Avatar.objects.create(user=user, image=formulario.cleaned_data.get("image"))

            print("avatar - Success!")
            avatar = Avatar.objects.get_or_create(user=user)[0]
            if avatar.image:
                request.session['avatar_url'] = avatar.image.url
            return redirect('index')
    formulario = AvatarFormulario()
    return render(request, 'usuario_avatar.html', {"form": formulario})
