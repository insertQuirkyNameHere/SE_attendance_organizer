# Generated by Django 3.2.8 on 2022-01-27 16:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20220127_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingrequests',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='requests',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
