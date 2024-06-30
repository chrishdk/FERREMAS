import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.branches.models import Branch

@pytest.mark.django_db
def test_get_branch_list():
    client = APIClient()
    Branch.objects.create(nombre="Sucursal 1", direccion="Dirección 1", telefono="123456789")
    Branch.objects.create(nombre="Sucursal 2", direccion="Dirección 2", telefono="987654321")

    url = reverse('branch-list')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_add_branch():
    client = APIClient()
    url = reverse('add-branch')
    data = {'nombre': 'Sucursal 1', 'direccion': 'Dirección 1', 'telefono': '123456789'}

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['nombre'] == 'Sucursal 1'
    assert Branch.objects.count() == 1


@pytest.mark.django_db
def test_add_branch_invalid_data():
    client = APIClient()
    url = reverse('add-branch')
    data = {'nombre': 'Sucursal 1', 'direccion': 'Dirección 1'}

    response = client.post(url, data, format='json')

    assert response.status_code == 400
    assert 'telefono' in response.data
    assert Branch.objects.count() == 0

    
@pytest.mark.django_db
def test_branch_detail_view():
    client = APIClient()
    branch = Branch.objects.create(nombre="Sucursal 1", direccion="Dirección 1", telefono="123456789")
    
    url = reverse('branch-detail', args=[branch.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['nombre'] == 'Sucursal 1'
    assert response.data['direccion'] == 'Dirección 1'
    assert response.data['telefono'] == '123456789'

