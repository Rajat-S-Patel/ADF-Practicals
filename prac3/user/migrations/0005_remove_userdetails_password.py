# Generated by Django 3.2.7 on 2021-09-21 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userdetails_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='password',
        ),
    ]
