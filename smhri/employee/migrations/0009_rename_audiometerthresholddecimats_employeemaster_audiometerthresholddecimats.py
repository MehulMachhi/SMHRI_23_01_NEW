# Generated by Django 4.1.4 on 2022-12-20 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_alter_employeemaster_audiometerthresholddecimats_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeemaster',
            old_name='audiometerThresholdDecimats',
            new_name='AudiometerThresholdDecimats',
        ),
    ]
