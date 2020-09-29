from django.urls import path

from pypro.modulos import views

app_name = 'modulos'

urlpatterns = [
    path('<slug:slug>', views.detalhes, name='detalhes'),
    path('<slug:slug>', views.aula, name='aula'),
]
