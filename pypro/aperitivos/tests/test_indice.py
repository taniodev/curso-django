import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize('titulo', [
    'Video Aperitivo: Motivação',
    'Instalação no Windows',
])
def test_titulo_do_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize('slug', [
    'motivacao',
    'instalacao-windows',
])
def test_link_do_video(resp, slug):
    link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{link}"')
