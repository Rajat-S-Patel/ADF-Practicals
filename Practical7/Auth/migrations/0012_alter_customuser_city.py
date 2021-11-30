# Generated by Django 3.2.6 on 2021-11-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0011_alter_customuser_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[('jodhpur', 'Jodhpur'), ('surat', 'Surat'), ('udaipur', 'Udaipur'), ('nagpur', 'Nagpur'), ('ahmedabad', 'Ahmedabad'), ('gandhinagar', 'Gandhinagar'), ('pune', 'Pune'), ('jaipur', 'Jaipur'), ('mumbai', 'Mumbai'), ('vadodara', 'Vadodara')], max_length=100),
        ),
    ]