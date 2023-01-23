# Generated by Django 4.1.4 on 2022-12-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_master', '0003_rename_xray_reports_audiometerthresholddecimats_xray_report'),
        ('employee', '0007_employeemaster_employee_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='audiometerThresholdDecimats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.audiometerthresholddecimats'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='bloodTest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.bloodtest'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='complaints',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.complaints'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='hematology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.hematology'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='lungFunctionTest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.lungfunctiontest'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='microscopicExamination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.microscopicexamination'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='otherTests',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.othertests'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='physiologicalTest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.physiologicaltest'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='systematicExamination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.systematicexamination'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='visualTest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_master.visualtest'),
        ),
    ]