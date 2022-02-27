from django.db import models
class Teachers(models.Model):
    f_name = models.CharField(max_length=30, verbose_name='Имя')
    s_name = models.CharField(max_length=30, verbose_name='Фамилия')
    class Meta:
        verbose_name = "Преподователь"
        verbose_name_plural = "Преподователи"
        
    def __str__(self):
        s = self.f_name + ' ' + self.s_name
        return s

 