from django.db import models
from services.models import Servise
from django.core.validators import RegexValidator

class Klients(models.Model):
    f_name = models.CharField(max_length=30, verbose_name='Имя')
    s_name = models.CharField(max_length=30, verbose_name='Фамилия')
    servise = models.ManyToManyField(Servise)
    town = models.CharField(max_length=30, verbose_name='Город')
    school = models.CharField(max_length=30, verbose_name='Школа')
    telephone = models.CharField(validators=[RegexValidator('^\+?1?\d{9,15}$')], max_length=17, blank=True)
    status = models.CharField(max_length=300)
    istochnik = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('f_name',)
    
    def __str__(self):
        s = self.f_name + ' ' + self.s_name
        return s

class KlientServise(models.Model):
        klient = models.ForeignKey(Klients, on_delete=models.CASCADE, null=False, verbose_name='Клиент')
        servise = models.ForeignKey(Servise, on_delete=models.CASCADE, null=False, verbose_name='Сервис')
        price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', blank=True)
