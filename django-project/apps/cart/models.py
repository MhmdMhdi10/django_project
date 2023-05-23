from django.db import models

from apps.core_app.models import BaseModel
from apps.product.models import Product
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Cart(BaseModel):
    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "carts"

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class CartItem(BaseModel):
    class Meta:
        verbose_name = "cart_item"
        verbose_name_plural = "cart_items"

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.cart}'
