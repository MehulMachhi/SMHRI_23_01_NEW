# Generated by Django 4.1.4 on 2023-01-18 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0022_alter_audiometerthresholddecimats_audiometery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodtest',
            name='blood_cholestrol',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
