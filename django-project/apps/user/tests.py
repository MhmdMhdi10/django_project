from django.contrib.auth import get_user_model
import pytest

User = get_user_model()


@pytest.fixture
def test_user():
    return User.objects.create_user(
        email='testuser@example.com',
        password='testpass',
        first_name='Test',
        last_name='User'
    )


def test_user_creation(test_user):
    assert test_user.email == 'testuser@example.com'
    assert test_user.first_name == 'Test'
    assert test_user.last_name == 'User'
    assert str(test_user) == 'testuser@example.com'
    assert test_user.get_full_name() == 'Test User'
    assert test_user.get_short_name() == 'Test'
    assert test_user.is_active == True
    assert test_user.is_staff == False


def test_superuser_creation():
    superuser = User.objects.create_superuser(
        email='superuser@example.com',
        password='superpass',
        first_name='Super',
        last_name='User'
    )

    assert superuser.email == 'superuser@example.com'
    assert superuser.first_name == 'Super'
    assert superuser.last_name == 'User'
    assert str(superuser) == 'superuser@example.com'
    assert superuser.get_full_name() == 'Super User'
    assert superuser.get_short_name() == 'Super'
    assert superuser.is_active == True
    assert superuser.is_staff == True
    assert superuser.is_superuser == True
