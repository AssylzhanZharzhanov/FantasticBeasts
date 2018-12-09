# Generated by Django 2.1.4 on 2018-12-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0006_auto_20181209_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2)),
            ],
        ),
    ]
