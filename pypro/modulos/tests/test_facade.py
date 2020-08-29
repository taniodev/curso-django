import pytest
from model_bakery import baker

from pypro.modulos import facade
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    titulos = ['antes', 'depois']
    return [baker.make(Modulo, titulo=t) for t in titulos]


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facade.listar_modulos_ordenados()
