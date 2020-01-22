from django.db import models
from KokoaPage.settings import MEDIA_URL


class Banner(models.Model):
    title = models.CharField(max_length=32)
    message = models.CharField(max_length=64)
    image = models.ImageField(upload_to=f'banners/')

    def __str__(self):
        return f'{self.title} {self.message}'
