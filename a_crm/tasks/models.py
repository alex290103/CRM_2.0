from django.db import models
from klients.models import Klients
from users.models import User

# Create your models here.

class Tasks(models.Model):
    klient = models.ForeignKey(Klients, related_name='tasks', on_delete=models.CASCADE, null=True, verbose_name='Клиент')
    task = models.TextField(max_length=100, verbose_name='Задача')
    deadline = models.DateField(verbose_name='Срок выполнения')
    checked = models.BooleanField(default=False, verbose_name='Выполнено')
    hr_manager = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, verbose_name='Пользователь')


    class Meta:
        verbose_name = ("Задача")
        verbose_name_plural = ("Задачи")
        ordering = ('checked','deadline')

    def __str__(self):
        return self.task
