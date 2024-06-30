import pytest
from apps.branches.models import Branch
from apps.branches.serializers import BranchSerializer


@pytest.mark.django_db
def test_create_branch():
    branch = Branch.objects.create(nombre="Sucursal 1", direccion="Dirección 1", telefono="123456789")
    assert branch.nombre == "Sucursal 1"
    assert branch.direccion == "Dirección 1"
    assert branch.telefono == "123456789"

@pytest.mark.django_db
def test_branch_serializer():
    data = {'nombre': 'Sucursal 1', 'direccion': 'Dirección 1', 'telefono': '123456789'}
    serializer = BranchSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data['nombre'] == 'Sucursal 1'
    assert serializer.validated_data['direccion'] == 'Dirección 1'
    assert serializer.validated_data['telefono'] == '123456789'

@pytest.mark.django_db
def test_branch_str_representation():
    branch = Branch(nombre="Sucursal 1", direccion="Dirección 1", telefono="123456789")
    assert str(branch) == "Sucursal 1"

@pytest.mark.django_db
def test_branch_serializer_missing_data():
    data = {'nombre': 'Sucursal 1', 'direccion': 'Dirección 1'}
    serializer = BranchSerializer(data=data)
    assert not serializer.is_valid()
    assert 'telefono' in serializer.errors