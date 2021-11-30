# Generated by Django 3.2.6 on 2021-11-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_alter_customuser_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[('gandhinagar', 'Gandhinagar'), ('pune', 'Pune'), ('jaipur', 'Jaipur'), ('udaipur', 'Udaipur'), ('ahmedabad', 'Ahmedabad'), ('mumbai', 'Mumbai'), ('vadodara', 'Vadodara'), ('jodhpur', 'Jodhpur'), ('surat', 'Surat'), ('nagpur', 'Nagpur')], max_length=100),
        ),
    ]