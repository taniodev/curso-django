from django.shortcuts import render

from pypro.modulos import facade


def detalhes(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhes.html', {'modulo': modulo, 'aulas': aulas})
