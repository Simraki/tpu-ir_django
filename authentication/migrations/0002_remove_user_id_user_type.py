# Generated by Django 3.2 on 2021-08-18 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_user_type',
        ),
    ]
