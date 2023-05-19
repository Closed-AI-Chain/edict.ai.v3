from django.db import models

# Create your models here.
class VideoLinks(models.Model):
   link=models.CharField(blank=False, max_length=300)