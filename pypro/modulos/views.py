from django.shortcuts import render

from pypro.modulos import facade


def detalhes(request, slug):
    modulo = facade.encontrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhes.html', {'modulo': modulo})
