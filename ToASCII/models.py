from django.db import models
from random import randint


class Image(models.Model):
    image = models.FileField(upload_to='source/')
