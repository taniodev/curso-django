from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> list:
    """Lista os módulos ordenados pela propriedade order"""
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    """Retorne um módulo do banco de dados correspondente ao slug"""
    return Modulo.objects.get(slug=slug)
