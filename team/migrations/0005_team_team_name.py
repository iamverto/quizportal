# Generated by Django 2.2.4 on 2019-08-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20190811_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(default='NO NAME PROVIDED', max_length=100),
            preserve_default=False,
        ),
    ]
