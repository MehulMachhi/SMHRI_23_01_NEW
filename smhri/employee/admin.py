from django.contrib import admin

# Register your models here.

from employee.models import EmployeeMaster

class EmployeeMasterAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'employee_no', 'aadhar_card_no',
                    )

    fieldsets = [
        ('Profile', {
            'fields': [ 'name_pref', 'first_name', 'middle_name', 'last_name', 'sex',
                        ],
        }),
        ('Company', {
            'classes': ['collapse'],
            'fields': ['company', 'employee_no', 'ticket_no', 'aadhar_card_no', 'pan_number'],
        }),
        ('Details', {

            'fields': ['date_joining',  'designation', 'department'],
        }),
        ('Contact', {
            'classes': ['collapse'],
            'fields': [ 'address', 'city', ],
        }),
        ('Info', {
            'classes': ['collapse'],
            'fields': ['birthdate', 'photo', 'fitness_certificate_date',  'previous_certificate_number' ],
        }),
        ('Add Test', {
            'classes': ['collapse'],
            'fields': ['collection_date', 'test_date', 'status' ,  'AudiometerThresholdDecimats', 'BloodTest',
                       'Complaints', 'Hematology' ,'LungFunctionTest', 'MicroscopicExamination', 'OtherTests', 'PhysiologicalTest',
                       'SystematicExamination', 'VisualTest'],
        }),

        # ('BloodTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('Complaints', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('Hematology', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('LungFunctionTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('MicroscopicExamination', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('OtherTests', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('PhysiologicalTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('SystematicExamination', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # ('VisualTest', {
        #     'classes': ['collapse'],
        #     'fields': [],
        # }),
        # # ('TestMaster', {
        # #     'classes': ['collapse'],
        # #     'fields': [],
        # # }),

    ]

    # def has_module_permission(self, request):
    #     return False



admin.site.register(EmployeeMaster, EmployeeMasterAdmin)