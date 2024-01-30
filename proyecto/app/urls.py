from django.urls import path, include
from django.contrib.auth.views import LogoutView
from app.views import (
    registrar,
    login_request,
    ArqueroList,
    ArqueroCreacion,
    ArqueroDetalle,
    ArqueroDelete, 
    ArqueroEditar,
    DefensorList,
    DefensorCreacion,
    DefensorDetalle,
    DefensorEditar,
    DefensorDelete,
    MediocampistaList,
    MediocampistaCreacion,
    MediocampistaDetalle,
    MediocampistaEditar,
    MediocampistaDelete,
    DelanteroList,
    DelanteroCreacion,
    DelanteroDetalle,
    DelanteroEditar,
    DelanteroDelete,
    #arquero_create,
    avatar,
    index)

urlpatterns = [
    path('registrar/', registrar, name = "registrar"),
    path('login/', login_request, name = 'login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = "Logout"),
    #CRUD Arquero
    path('arquero/list', ArqueroList.as_view(), name = 'ArqueroList'),
    path('crear-arquero/', ArqueroCreacion.as_view(), name = 'ArqueroCreacion'),
    path('detalle-arquero/<pk>', ArqueroDetalle.as_view(), name = 'ArqueroDetalle'),
    path('editar-arquero/<pk>', ArqueroEditar.as_view(), name = 'ArqueroEditar'),
    path('borrar-arquero/<pk>', ArqueroDelete.as_view(), name = 'ArqueroDelete'),
    #CRUD Defensor
    path('defensor/list', DefensorList.as_view(), name = 'DefensorList'),
    path('crear-defensor/', DefensorCreacion.as_view(), name = 'DefensorCreacion'),
    path('detalle-defensor/<pk>', DefensorDetalle.as_view(), name = 'DefensorDetalle'),
    path('editar-defensor/<pk>', DefensorEditar.as_view(), name = 'DefensorEditar'),
    path('borrar-defensor/<pk>', DefensorDelete.as_view(), name = 'DefensorDelete'),
    #CRUD Mediocampista
    path('mediocampista/list', MediocampistaList.as_view(), name = 'MediocampistaList'),
    path('crear-mediocampista/', MediocampistaCreacion.as_view(), name = 'MediocampistaCreacion'),
    path('detalle-mediocampista/<pk>', MediocampistaDetalle.as_view(), name = 'MediocampistaDetalle'),
    path('editar-mediocampista/<pk>', MediocampistaEditar.as_view(), name = 'MediocampistaEditar'),
    path('borrar-mediocampista/<pk>', MediocampistaDelete.as_view(), name = 'MediocampistaDelete'),
    #CRUD Delantero
    path('delantero/list', DelanteroList.as_view(), name = 'DelanteroList'),
    path('crear-delantero/',DelanteroCreacion.as_view(), name = 'DelanteroCreacion'),
    path('detalle-delantero/<pk>', DelanteroDetalle.as_view(), name = 'DelanteroDetalle'),
    path('editar-delantero/<pk>', DelanteroEditar.as_view(), name = 'DelanteroEditar'),
    path('borrar-delantero/<pk>', DelanteroDelete.as_view(), name = 'DelanteroDelete'),
    #Avartar del usuario
    path('avatar', avatar, name='avatar'),
    path('', index, name = 'index'),
]

