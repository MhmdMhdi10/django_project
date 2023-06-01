from django.contrib.auth.models import BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Users must have email address")

        email = self.normalize_email(email)

        print(email)

        user = self.model(email=email, **extra_fields)

        print(user)

        user.set_password(password)

        try:
            user.save(using=self._db)
        except Exception as e:
            print(e)

        return user

    def create_manager(self, email, password, **extra_fields):

        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = False
        user.is_manager = True
        user.is_staff = True
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_manager = True
        user.is_staff = True
        user.save()

        return user
