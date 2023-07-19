# Generated by Django 3.2.20 on 2023-07-19 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='users.user'),
        ),
        migrations.AddField(
            model_name='task',
            name='proposer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to='users.user'),
            preserve_default=False,
        ),
    ]
