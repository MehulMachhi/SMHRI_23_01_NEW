# Generated by Django 4.1.4 on 2022-12-21 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_companymaster_company_registration_certificate'),
        ('employee', '0013_alter_employeemaster_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='company_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companymaster'),
        ),
    ]
