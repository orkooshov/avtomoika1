from django.db import models

from core.models import AbstractTimestampedModel


class AbstractProfile(AbstractTimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    photo = models.ImageField(
        'Фото', blank=True, upload_to='avatars/')

    class Meta:
        abstract = True


class ClientProfile(AbstractProfile):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Staff(AbstractProfile):
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
