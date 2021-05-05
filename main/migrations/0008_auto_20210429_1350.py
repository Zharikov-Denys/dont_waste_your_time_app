# Generated by Django 3.2 on 2021-04-29 10:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_alter_projects_activity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activities',
            options={'verbose_name': 'Вид деятельности', 'verbose_name_plural': 'Виды деятельности'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.activities', verbose_name='Вид деятельности'),
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('start', models.TimeField(default=datetime.time(0, 0), verbose_name='Начало')),
                ('end', models.TimeField(default=datetime.time(0, 0), verbose_name='Конец')),
                ('duration', models.TimeField(default=datetime.time(0, 0), verbose_name='Время')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.activities', verbose_name='Вид деятельности')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.projects', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]