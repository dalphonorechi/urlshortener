from django.db import models

# Create your models here.
class UrlObj(models.Model):
    original_url = models.CharField(max_length=255)

