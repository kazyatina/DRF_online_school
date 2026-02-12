from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150, verbose_name="Ник", unique=False)
    email = models.EmailField(unique=True)

    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Телефон"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="Аватар"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
