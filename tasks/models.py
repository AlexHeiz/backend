from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField('Название', max_length=20, blank=False)
    description = models.TextField('Описание', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField('Выполнение', default=False)

    def __int__(self):
        return self.pk

    class Meta():
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'