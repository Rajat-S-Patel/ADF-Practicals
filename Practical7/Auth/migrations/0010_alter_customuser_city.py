# Generated by Django 3.2.6 on 2021-11-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0009_alter_customuser_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[('mumbai', 'Mumbai'), ('jaipur', 'Jaipur'), ('gandhinagar', 'Gandhinagar'), ('jodhpur', 'Jodhpur'), ('surat', 'Surat'), ('vadodara', 'Vadodara'), ('pune', 'Pune'), ('nagpur', 'Nagpur'), ('ahmedabad', 'Ahmedabad'), ('udaipur', 'Udaipur')], max_length=100),
        ),
    ]
