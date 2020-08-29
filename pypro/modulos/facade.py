from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> list:
    """Lista os módulos ordenados pela propriedade order"""
    return list(Modulo.objects.order_by('order').all())
