from django.db import models
from django.contrib.auth import get_user_model
from apps.core_app.models import BaseModel
from apps.coupons.models import Coupon
from apps.product.models import Product

User = get_user_model()


class Order(BaseModel):
    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    class OrderStatus(models.TextChoices):
        not_processed = 'not_processed'
        processed = 'processed'
        shipping = 'shipped'
        delivered = 'delivered'
        cancelled = 'cancelled'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.OneToOneField(Coupon, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    shipping_name = models.CharField(max_length=255)
    shipping_price = models.DecimalField(max_digits=5, decimal_places=2)
    shipping_time = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50, choices=OrderStatus.choices, default=OrderStatus.not_processed)


class OrderItem(BaseModel):
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    class OrderItemStatus(models.TextChoices):
        not_processed = 'not_processed'
        processed = 'processed'
        shipping = 'shipped'
        delivered = 'delivered'
        cancelled = 'cancelled'

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
    status = models.CharField(
        max_length=50, choices=OrderItemStatus.choices, default=Order.OrderStatus.not_processed)

    def __str__(self):
        return self.name
