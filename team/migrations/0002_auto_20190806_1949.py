# Generated by Django 2.2.4 on 2019-08-06 19:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='participants',
        ),
        migrations.AddField(
            model_name='team',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
