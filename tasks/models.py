from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField('Название', max_length=20, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


    class Meta():
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

