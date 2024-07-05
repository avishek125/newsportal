from django.db import models

# Create your models here.
class News(models.Model):
    title = models.charfield(max_length=255)
    image = models.imagefield()