# Generated by Django 4.1.4 on 2023-01-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_companymaster_company_registration_certificate'),
        ('employee', '0025_remove_employeemaster_list_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='list_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.companymaster'),
        ),
    ]
