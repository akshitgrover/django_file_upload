from django.db import models

class file(models.Model):
    file = models.FileField(upload_to='documents/')
    name = models.CharField(max_length=10)