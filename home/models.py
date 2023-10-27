from django.db import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="upload/")
