# Generated by Django 4.0 on 2022-01-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('s_name', models.CharField(max_length=30, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Преподователь',
                'verbose_name_plural': 'Преподователи',
            },
        ),
    ]