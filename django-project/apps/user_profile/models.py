from django.core.validators import RegexValidator
from django.db import models
from apps.core_app.models import BaseModel
from django.conf import settings
from apps.core_app.cities import Cities


User = settings.AUTH_USER_MODEL
domain = settings.DOMAIN


class Address(BaseModel):
    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"

    body = models.TextField()
    city = models.CharField(max_length=255, choices=Cities.choices, default=Cities.Tehran)

    def __str__(self):
        return self.body


class UserProfile(BaseModel):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address', blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone = models.IntegerField(validators=[phone_regex], max_length=17)
    image = models.ImageField(upload_to='profiles/%Y/%m/')
