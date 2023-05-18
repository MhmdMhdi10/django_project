import pytest
from django.contrib.auth import get_user_model
from apps.product.models import Product
from .models import Order, OrderItem
from datetime import datetime
from decimal import Decimal

User = get_user_model()

@pytest.fixture
def test_user():
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def test_product():
    return Product.objects.create(name='Test Product', price=10)

@pytest.fixture
def test_order(test_user):
    return Order.objects.create(
        status='not_processed',
        user=test_user,
        transaction_id='testtransaction',
        amount=10.99,
        full_name='Test User',
        address_line_1='123 Main St',
        city='Testville',
        state_province_region='Test State',
        postal_zip_code='12345',
        country_region='Peru',
        telephone_number='555-555-5555',
        shipping_name='Test Shipping',
        shipping_time='1-3 days',
        shipping_price=5.99,
        date_issued=datetime.now()
    )

@pytest.fixture
def test_order_item(test_product, test_order):
    return OrderItem.objects.create(
        product=test_product,
        order=test_order,
        name='Test Product',
        price=10,
        count=1,
        date_added=datetime.now()
    )

def test_order_creation(test_order, test_user):
    assert test_order.status == 'not_processed'
    assert test_order.user == test_user
    assert test_order.transaction_id == 'testtransaction'
    assert test_order.amount == Decimal('10.99')
    assert test_order.full_name == 'Test User'
    assert test_order.address_line_1 == '123 Main St'
    assert test_order.city == 'Testville'
    assert test_order.state_province_region == 'Test State'
    assert test_order.postal_zip_code == '12345'
    assert test_order.country_region == 'Peru'
    assert test_order.telephone_number == '555-555-5555'
    assert test_order.shipping_name == 'Test Shipping'
    assert test_order.shipping_time == '1-3 days'
    assert test_order.shipping_price == Decimal('5.99')
    assert isinstance(test_order.date_issued, datetime)
    assert str(test_order) == 'testtransaction'

def test_order_item_creation(test_order_item, test_product, test_order):
    assert test_order_item.product == test_product
    assert test_order_item.order == test_order
    assert test_order_item.name == 'Test Product'
    assert test_order_item.price == Decimal('10')
    assert test_order_item.count == 1
    assert isinstance(test_order_item.date_added, datetime)
    assert str(test_order_item) == 'Test Product'