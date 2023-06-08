from django.test import TestCase
from .models import UserAccount


class UserAccountTestCase(TestCase):
    def setUp(self):
        UserAccount.objects.create_user(
            email='m@gmail.com',
            first_name='mahdi',
            last_name='f',
            password='12345678Lte'
        )

    def test_user_account(self):
        user = UserAccount.objects.get(
            email='m@gmail.com'
        )
        self.assertEqual(user.first_name, 'mahdi')
        self.assertEqual(user.last_name, 'f')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertNotEqual(user.first_name, 'mahdi1')
        self.assertNotEqual(user.last_name, 'f1')
        self.assertNotEqual(user.is_active, False)
        self.assertNotEqual(user.is_staff, True)

    def test_get_full_name(self):
        user = UserAccount.objects.get(
            email='m@gmail.com'
        )
        self.assertEqual(user.get_full_name(), 'mahdi f')

    def test_short_name(self):
        user = UserAccount.objects.get(
            email='m@gmail.com'
        )
        self.assertEqual(user.get_short_name(), 'mahdi')

    def test_str(self):
        user = UserAccount.objects.get(
            email='m@gmail.com'
        )
        self.assertEqual(user.__str__(), 'm@gmail.com')
