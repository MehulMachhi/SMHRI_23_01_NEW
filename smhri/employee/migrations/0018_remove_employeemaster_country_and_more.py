# Generated by Django 4.1.4 on 2022-12-23 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_alter_employeemaster_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemaster',
            name='country',
        ),
        migrations.RemoveField(
            model_name='employeemaster',
            name='state',
        ),
    ]
