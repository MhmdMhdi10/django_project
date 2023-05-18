import pytest
from django.contrib.auth import get_user_model
from apps.product.models import Product
from .models import Cart, CartItem

User = get_user_model()


@pytest.fixture
def test_user():
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def test_cart(test_user):
    return Cart.objects.create(user=test_user)


@pytest.fixture
def test_product():
    return Product.objects.create(name='Test Product', price=10)


def test_cart_creation(test_user):
    cart = Cart.objects.create(user=test_user)
    assert cart.user == test_user
    assert cart.total_items == 0


def test_cart_item_creation(test_cart, test_product):
    cart_item = CartItem.objects.create(cart=test_cart, product=test_product, count=2)
    assert cart_item.cart == test_cart
    assert cart_item.product == test_product
    assert cart_item.count == 2
