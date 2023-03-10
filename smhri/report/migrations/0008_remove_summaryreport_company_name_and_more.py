# Generated by Django 4.1.4 on 2023-01-18 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0026_employeemaster_list_company'),
        ('report', '0007_delete_employeereports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summaryreport',
            name='company_name',
        ),
        migrations.AddField(
            model_name='summaryreport',
            name='employee_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.employeemaster'),
            preserve_default=False,
        ),
    ]
