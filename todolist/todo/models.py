from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class Uzduotis(models.Model):
    title = models.TextField('Pavadinimas', max_length=200)
    body = models.CharField('Tekstas', max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uzduotys')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.title}, ({self.body}), {self.data}"

    def get_absolute_url(self):
        return reverse('uzduotis', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Užduotis'
        verbose_name_plural = 'Užduotys'
        ordering = ['-data']
