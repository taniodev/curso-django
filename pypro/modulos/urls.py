from django.urls import path

from pypro.modulos.views import detalhes

app_name = 'modulos'

urlpatterns = [
    path('<slug:slug>', detalhes, name='detalhes'),
]
