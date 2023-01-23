from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CompanyMaster(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField(null=True, blank=True,)
    pincode = models.IntegerField()
    company_registration_certificate = models.ImageField(upload_to='media', max_length=222, null=True)
    address = models.CharField(max_length=200, null=True)
    class country(models.TextChoices):
        India = 'India', ('India')
        Australia = 'Australia', ('Australia')
        Uk = 'Uk', ('Uk')
    country = models.CharField(choices=country.choices, max_length=222, null=True, blank=True,)
    class test(models.TextChoices):
        AudiometerThresholdDecimats = 'AudiometerThresholdDecimats', ('AudiometerThresholdDecimats')
        BloodTest = 'BloodTest', ('BloodTest')
        Complaints = 'Complaints', ('Complaints')
        Hematology = 'Hematology', ('Hematology')
        LungFunctionTest = 'LungFunctionTest', ('LungFunctionTest')
        MicroscopicExamination = 'MicroscopicExamination', ('MicroscopicExamination')
        OtherTests = 'OtherTests', ('OtherTests')
        PhysiologicalTest = 'PhysiologicalTest', ('PhysiologicalTest')
        SystematicExamination = 'SystematicExamination', ('SystematicExamination')
        VisualTest = 'VisualTest', ('VisualTest')
    test = models.CharField(choices=test.choices, max_length=222, null=True, blank=True)

    def __str__(self):
        return self.name










