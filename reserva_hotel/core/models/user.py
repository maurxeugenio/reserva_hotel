from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile = models.OneToOneField(
        'core.Profile',
        on_delete=models.SET_NULL,
        null=True
    )
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_owner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    active_company = models.ForeignKey(
        'core.Company',
        null=True,
        on_delete=models.SET_NULL
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    phone = models.CharField(
        max_length=200, default=''
    )
    document = models.CharField(max_length=200, default='')

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
