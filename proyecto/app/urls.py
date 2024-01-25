from django.urls import path, include
from django.contrib.auth.views import LogoutView
from app.views import (
    registrar,
    login, 
    index)

urlpatterns = [
    path('registrar/', registrar, name = "registrar"),
    path('login/', login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = "Logout"),
    path('', index, name = 'index'),
]

