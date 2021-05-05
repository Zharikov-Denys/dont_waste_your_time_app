# Generated by Django 3.2 on 2021-04-30 18:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210429_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['-date', '-end'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='projects',
            name='total_time',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Потрачено времени'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.projects', verbose_name='Проект'),
        ),
    ]
