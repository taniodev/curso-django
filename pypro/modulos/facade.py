from pypro.modulos.models import Aula, Modulo


def listar_modulos_ordenados() -> list:
    """Lista os módulos ordenados pela propriedade order"""
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    """Retorne um módulo do banco de dados correspondente ao slug"""
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    return Modulo.objects.order_by('order').all()
