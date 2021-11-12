# Generated by Django 3.2.6 on 2021-11-11 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auth', '0004_auto_20211110_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(default='resume/default.pdf', upload_to='resume/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('mumbai', 'Mumbai'), ('pune', 'Pune'), ('gandhinagar', 'Gandhinagar'), ('udaipur', 'Udaipur'), ('nagpur', 'Nagpur'), ('ahmedabad', 'Ahmedabad'), ('surat', 'Surat'), ('jodhpur', 'Jodhpur'), ('jaipur', 'Jaipur'), ('vadodara', 'Vadodara')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_photos/default.jpg', upload_to='profile_photos/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
