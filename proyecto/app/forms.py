from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArqueroFormulario (forms.Form):
    descripcion = forms.CharField(max_length=300)

class DefensorFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pie_habil = forms.CharField(max_length=20)
    cant_clubes_anteriores = forms.IntegerField()
    telefono =forms.IntegerField()
    estatura = forms.FloatField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()

class MediocampistaFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pie_habil = forms.CharField(max_length=20)
    cant_clubes_anteriores = forms.IntegerField()
    telefono =forms.IntegerField()
    estatura = forms.FloatField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()

class DelanteroFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pie_habil = forms.CharField(max_length=20)
    cant_clubes_anteriores = forms.IntegerField()
    telefono =forms.IntegerField()
    estatura = forms.FloatField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()

class UserRegistrationForm (UserCreationForm):
    last_name = forms.CharField()
    first_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class AvatarFormulario(forms.Form):
    image = forms.ImageField()

class UserEditForm (UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']