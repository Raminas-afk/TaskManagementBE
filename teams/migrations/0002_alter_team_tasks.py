# Generated by Django 3.2.20 on 2023-07-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='tasks',
            field=models.ManyToManyField(blank=True, null=True, related_name='teams', to='tasks.Task'),
        ),
    ]
