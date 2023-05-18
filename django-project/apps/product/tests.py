import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.category.models import Category
from .models import Product
from datetime import datetime


@pytest.fixture
def test_category():
    return Category.objects.create(name='Test Category')


@pytest.fixture
def test_product():
    photo = SimpleUploadedFile(
        name='test_product_photo.jpg',
        content=open('test_product_photo.jpg', 'rb').read(),
        content_type='image/jpeg'
    )
    return Product.objects.create(
        name='Test Product',
        photo=photo,
        description='Test description',
        price=10.99,
        compare_price=9.99,
        category=test_category(),
        quantity=10,
        sold=0,
        date_created=datetime.now()
    )


def test_product_creation(test_product):
    assert test_product.name == 'Test Product'
    assert test_product.photo.name == 'photos/{}/{}.jpg'.format(datetime.now().strftime('%Y'),
                                                                datetime.now().strftime('%m'))
    assert test_product.description == 'Test description'
    assert test_product.price == 10.99
    assert test_product.compare_price == 9.99
    assert test_product.category.name == 'Test Category'
    assert test_product.quantity == 10
    assert test_product.sold == 0
    assert isinstance(test_product.date_created, datetime)
    assert str(test_product) == 'Test Product'


def test_get_thumbnail(test_product):
    assert test_product.get_thumbnail() == '/media/photos/{}/{}.jpg'.format(datetime.now().strftime('%Y'),
                                                                            datetime.now().strftime('%m'))
