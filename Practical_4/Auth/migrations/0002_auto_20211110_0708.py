# Generated by Django 3.2.6 on 2021-11-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('surat', 'Surat'), ('nagpur', 'Nagpur'), ('jaipur', 'Jaipur'), ('ahmedabad', 'Ahmedabad'), ('mumbai', 'Mumbai'), ('udaipur', 'Udaipur'), ('vadodara', 'Vadodara'), ('gandhinagar', 'Gandhinagar'), ('jodhpur', 'Jodhpur'), ('pune', 'Pune')], max_length=50),
        ),
    ]
