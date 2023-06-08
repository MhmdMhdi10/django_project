from django.test import TestCase
from .models import WishList, WishListItem
from ..user.models import UserAccount


class WishListTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='m@gmail.com',
            first_name='mahdi',
            last_name='f',
            password='12345678Lte'
        )
        WishList.objects.create(user=user)


