import pytest
from .models import FixedPriceCoupon, PercentageCoupon

@pytest.fixture
def test_fixed_price_coupon():
    return FixedPriceCoupon.objects.create(
        name='Test Coupon',
        discount_price=5.99
    )

@pytest.fixture
def test_percentage_coupon():
    return PercentageCoupon.objects.create(
        name='Test Coupon',
        discount_percentage=20
    )

def test_fixed_price_coupon_creation(test_fixed_price_coupon):
    assert test_fixed_price_coupon.name == 'Test Coupon'
    assert test_fixed_price_coupon.discount_price == 5.99
    assert str(test_fixed_price_coupon) == 'Test Coupon'

def test_percentage_coupon_creation(test_percentage_coupon):
    assert test_percentage_coupon.name == 'Test Coupon'
    assert test_percentage_coupon.discount_percentage == 20
    assert str(test_percentage_coupon) == 'Test Coupon'