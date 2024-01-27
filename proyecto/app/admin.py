from django.contrib import admin

# Register your models here.
from app.models import Arquero, Defensor, Mediocampista, Delantero, Avatar


admin.site.register(Arquero)
admin.site.register(Defensor)
admin.site.register(Mediocampista)
admin.site.register(Delantero)
admin.site.register(Avatar)
