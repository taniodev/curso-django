import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.modulos.models import Aula, Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(baker.make(Aula, 3, modulo=modulo))
    return aulas


@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice'))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200
