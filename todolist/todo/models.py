from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Uzduotis(models.Model):
    title = models.TextField('Pavadinimas', max_length=200)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField('Laikas', null=True)

    class Meta:
        verbose_name = 'Užduotis'
        verbose_name_plural = 'Užduotys'
        ordering = ['-data']
