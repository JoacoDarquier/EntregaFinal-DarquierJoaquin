from django.urls import path, include
from django.contrib.auth.views import LogoutView
from app.views import (
    registrar,
    login,
    ArqueroList,
    ArqueroCreacion,
    ArqueroDetalle,
    ArqueroDelete, 
    ArqueroEditar,
    index)

urlpatterns = [
    path('registrar/', registrar, name = "registrar"),
    path('login/', login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = "Logout"),
    path('arquero/list', ArqueroList.as_view(), name = 'List'),
    path('crear-arquero/', ArqueroCreacion.as_view(), name = 'New'),
    path('detalle-arquero/<pk>', ArqueroDetalle.as_view(), name = 'Detail'),
    path('editar-arquero/<pk>', ArqueroEditar.as_view(), name = 'Edit'),
    path('borrar-arquero/<pk>', ArqueroDelete.as_view(), name = 'Delete'),
    path('', index, name = 'index'),
]

