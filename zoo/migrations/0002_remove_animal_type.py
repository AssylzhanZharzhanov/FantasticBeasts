# Generated by Django 2.1.3 on 2018-11-27 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='type',
        ),
    ]
