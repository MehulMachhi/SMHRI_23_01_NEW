# Generated by Django 4.1.4 on 2022-12-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companymaster',
            name='city',
        ),
        migrations.RemoveField(
            model_name='companymaster',
            name='company_type',
        ),
        migrations.AddField(
            model_name='companymaster',
            name='country',
            field=models.CharField(blank=True, choices=[('India', 'India'), ('Australia', 'Australia'), ('Uk', 'Uk')], max_length=222, null=True),
        ),
        migrations.AddField(
            model_name='companymaster',
            name='pincode',
            field=models.IntegerField(max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='companymaster',
            name='test',
            field=models.CharField(blank=True, choices=[('Test1', 'Test1'), ('Test2', 'Test2'), ('Test3', 'Test3'), ('Test4', 'Test4'), ('Test5', 'Test5')], max_length=222, null=True),
        ),
    ]
