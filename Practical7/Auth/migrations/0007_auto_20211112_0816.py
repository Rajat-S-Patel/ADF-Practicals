# Generated by Django 3.2.6 on 2021-11-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0006_alter_customuser_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[('surat', 'Surat'), ('ahmedabad', 'Ahmedabad'), ('gandhinagar', 'Gandhinagar'), ('vadodara', 'Vadodara'), ('jodhpur', 'Jodhpur'), ('udaipur', 'Udaipur'), ('pune', 'Pune'), ('nagpur', 'Nagpur'), ('jaipur', 'Jaipur'), ('mumbai', 'Mumbai')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
