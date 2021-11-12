# Generated by Django 3.2.6 on 2021-11-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Auth', '0002_alter_customuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[('gandhinagar', 'Gandhinagar'), ('vadodara', 'Vadodara'), ('mumbai', 'Mumbai'), ('udaipur', 'Udaipur'), ('ahmedabad', 'Ahmedabad'), ('nagpur', 'Nagpur'), ('surat', 'Surat'), ('pune', 'Pune'), ('jaipur', 'Jaipur'), ('jodhpur', 'Jodhpur')], max_length=100),
        ),
    ]