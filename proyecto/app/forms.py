from django import forms

class ArqueroFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pie_habil = forms.CharField(max_length=20)
    cant_clubes_anteriores = forms.IntegerField()
    telefono =formss.IntegerField()
    estatura = forms.FloatField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()

class DefensorFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pie_habil = forms.CharField(max_length=20)
    cant_clubes_anteriores = forms.IntegerField()
    telefono =formss.IntegerField()
    estatura = forms.FloatField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()

class MediocampistaFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pie_habil = forms.CharField(max_length=20)
    cant_clubes_anteriores = forms.IntegerField()
    telefono =formss.IntegerField()
    estatura = forms.FloatField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()

class DelanteroFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pie_habil = forms.CharField(max_length=20)
    cant_clubes_anteriores = forms.IntegerField()
    telefono =formss.IntegerField()
    estatura = forms.FloatField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()