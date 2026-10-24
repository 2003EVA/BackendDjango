from django.db import models

class profile(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.EmailField()