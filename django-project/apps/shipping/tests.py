import pytest
from .models import Shipping


@pytest.fixture
def test_shipping():
    return Shipping.objects.create(
        name='Test Shipping',
        time_to_delivery='1-3 days',
        price='10.99'
    )


@pytest.mark.django_db
def test_shipping_creation(test_shipping):
    assert test_shipping.name == 'Test Shipping'
    assert test_shipping.time_to_delivery == '1-3 days'
    assert test_shipping.price == 10.99
    assert str(test_shipping) == 'Test Shipping'

