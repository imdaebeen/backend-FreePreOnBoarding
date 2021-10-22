from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
import pytest

@pytest.fixture
def api_client():
    user = User.objects.create_user(username='daebeen', email='daebeen.im@naver.com', password='dlaeoqls!@#$90 ')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client

@pytest.mark.django_db
def test_get_post(api_client):
    url = reverse('get_post')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_post_post(api_client):
    url = reverse('get_post')
    response = api_client.post(url,{'title':'test data title'},{'post':'test data post'},{'author':'{api_client.user}'})
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_put_post(api_client):
    url = reverse('get_delete_update_post')
    response = api_client.put(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_delete_post(api_client):
    url = reverse('get_delete_update_post')
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_200_OK

