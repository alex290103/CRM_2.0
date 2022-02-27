# Generated by Django 4.0 on 2022-01-23 12:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('s_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('town', models.CharField(max_length=30, verbose_name='Город')),
                ('school', models.CharField(max_length=30, verbose_name='Школа')),
                ('telephone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')])),
                ('status', models.CharField(choices=[('Инт', 'Интересуется'), ('Зарег', 'Зарегистрирован'), ('Кл', 'Клиент')], max_length=300)),
                ('istochnik', models.CharField(choices=[('Сайт', 'Сайт'), ('Звонок', 'Звонок'), ('Рек', 'Реклама'), ('Уже', 'Уже клиент')], max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('servise', models.ManyToManyField(to='services.Servise')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('f_name',),
            },
        ),
        migrations.CreateModel(
            name='KlientServise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klients.klients', verbose_name='Клиент')),
                ('servise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servise', verbose_name='Сервис')),
            ],
        ),
    ]
