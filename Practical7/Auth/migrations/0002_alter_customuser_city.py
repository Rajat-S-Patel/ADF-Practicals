# Generated by Django 3.2.6 on 2021-11-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[('pune', 'Pune'), ('mumbai', 'Mumbai'), ('nagpur', 'Nagpur'), ('surat', 'Surat'), ('jaipur', 'Jaipur'), ('vadodara', 'Vadodara'), ('jodhpur', 'Jodhpur'), ('gandhinagar', 'Gandhinagar'), ('udaipur', 'Udaipur'), ('ahmedabad', 'Ahmedabad')], max_length=100),
        ),
    ]