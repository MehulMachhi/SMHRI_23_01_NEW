# Generated by Django 4.1.4 on 2022-12-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_companymaster_company_registration_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymaster',
            name='company_registration_certificate',
            field=models.ImageField(max_length=222, null=True, upload_to='media'),
        ),
    ]
