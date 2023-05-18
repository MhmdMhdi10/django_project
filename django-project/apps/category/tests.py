import pytest
from .models import Category


@pytest.fixture
def test_category():
    return Category.objects.create(name='Test Category')


def test_category_creation(test_category):
    assert test_category.name == 'Test Category'
    assert str(test_category) == 'Test Category'


def test_category_children():
    parent = Category.objects.create(name='Parent Category')
    child1 = Category.objects.create(name='Child Category 1', parent=parent)
    child2 = Category.objects.create(name='Child Category 2', parent=parent)

    assert parent.children.count() == 2
    assert child1.parent == parent
    assert child2.parent == parent
