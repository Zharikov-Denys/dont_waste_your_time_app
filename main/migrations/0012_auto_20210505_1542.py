# Generated by Django 3.2 on 2021-05-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_tasks_activity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['-created'], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AddField(
            model_name='tasks',
            name='ending_in_next_day',
            field=models.BooleanField(default=False, verbose_name='Заканчивается на следующий день'),
        ),
    ]
