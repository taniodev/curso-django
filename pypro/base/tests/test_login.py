import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('login'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    senha = "uma senha qualquer"
    usuario = baker.make(django_user_model)
    usuario.set_password(senha)
    usuario.save()
    usuario.senha_plana = senha
    return usuario


@pytest.fixture
def resp_post(client, usuario):
    resp = client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})
    return resp


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')


@pytest.fixture
def resp_home(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_botao_entrar_presente(resp_home):
    assert_contains(resp_home, 'Entrar')


def test_link_de_login_presente(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado, db):
    resp = client_com_usuario_logado.get(reverse('base:home'))
    return resp


def test_botao_entrar_ausente(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, 'Entrar')


def test_link_de_login_ausente(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, reverse('login'))


def test_nome_usuario_logado_presente(resp_home_com_usuario_logado, usuario_logado):
    assert_contains(resp_home_com_usuario_logado, usuario_logado.first_name)


def test_botao_sair_presente(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, 'Sair')


def test_link_de_logout_presente(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, reverse('logout'))
