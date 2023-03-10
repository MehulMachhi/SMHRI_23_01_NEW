# Generated by Django 4.1.4 on 2022-12-13 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test_master', '0003_rename_xray_reports_audiometerthresholddecimats_xray_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=20, null=True)),
                ('ticket_no', models.IntegerField(blank=True, null=True)),
                ('aadhar_card_no', models.IntegerField(blank=True, null=True)),
                ('name_pref', models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.')], max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('pan_number', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'male'), ('Female', 'female')], max_length=6, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('date_joining', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('test_type', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('approved', 'approved'), ('pending', 'pending')], max_length=8, null=True)),
                ('collection_date', models.DateTimeField(blank=True, null=True)),
                ('test_date', models.DateTimeField(blank=True, null=True)),
                ('fitness_certificate_date', models.DateTimeField(blank=True, null=True)),
                ('previous_certificate_number', models.IntegerField(blank=True, null=True)),
                ('emp_added_date', models.DateTimeField()),
                ('audiometerThresholdDecimats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.audiometerthresholddecimats')),
                ('bloodTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.bloodtest')),
                ('complaints', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.complaints')),
                ('hematology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.hematology')),
                ('lungFunctionTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.lungfunctiontest')),
                ('microscopicExamination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.microscopicexamination')),
                ('otherTests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.othertests')),
                ('physiologicalTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.physiologicaltest')),
                ('systematicExamination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.systematicexamination')),
                ('testMaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.testmaster')),
                ('visualTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_master.visualtest')),
            ],
        ),
    ]
