from django.db import models
from teachers.models import Teachers

class Servise(models.Model):
    TYPE_CHOICES = (
        ('Кр','Кружок'),
        ('Факульт','Факультатив'),
        ('Репет','Репетитор'),
    )
    name = models.CharField(max_length=30, verbose_name='Название')
    type = models.CharField(max_length=300, choices = TYPE_CHOICES)
    teacher = models.ManyToManyField(Teachers, related_name='servises')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class TeacherServise(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=False, verbose_name='Учитель')
    servise = models.ForeignKey(Servise, on_delete=models.CASCADE, null=False, verbose_name='Сервис')
    max_count = models.IntegerField(null=True, verbose_name='Количество клиентов в группе', blank=True)
    time = models.IntegerField(null=True, verbose_name='Количество часов')
