from django.db import models
from django.contrib import admin

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_images', blank=False)

admin.site.register(Image)
