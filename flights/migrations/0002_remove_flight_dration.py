# Generated by Django 2.1.3 on 2018-12-01 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='dration',
        ),
    ]
