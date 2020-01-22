from django.db import models
from KokoaPage.settings import MEDIA_URL


class Banner(models.Model):
    title = models.CharField(max_length=32)
    message = models.CharField(max_length=64)
    image = models.ImageField(upload_to=f'banners/')

    def __str__(self):
        return f'{self.title} {self.message}'


class Member(models.Model):
    name = models.CharField(max_length=64)
    major = models.CharField(max_length=32)
    join_year = models.IntegerField()
    is_senior = models.BooleanField()
    was_kore = models.BooleanField()
    is_kore = models.BooleanField()
    image = models.ImageField(upload_to=f'members/')

    def __str__(self):
        return f'{self.name} {self.major}'
