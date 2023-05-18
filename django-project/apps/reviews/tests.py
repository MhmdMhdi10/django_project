import pytest
from django.contrib.auth import get_user_model
from apps.product.models import Product
from .models import Review
from datetime import datetime

User = get_user_model()


@pytest.fixture
def test_user():
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def test_product():
    return Product.objects.create(name='Test Product', price=10)


@pytest.fixture
def test_review(test_user, test_product):
    return Review.objects.create(
        user=test_user,
        product=test_product,
        rating=4.5,
        comment='Test comment',
        date_created=datetime.now()
    )


def test_review_creation(test_review, test_user, test_product):
    assert test_review.user == test_user
    assert test_review.product == test_product
    assert test_review.rating == 4.5
    assert test_review.comment == 'Test comment'
    assert isinstance(test_review.date_created, datetime)
    assert str(test_review) == 'Test comment'
