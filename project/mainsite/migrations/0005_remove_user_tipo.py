# Generated by Django 3.1.2 on 2020-11-17 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20201105_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tipo',
        ),
    ]