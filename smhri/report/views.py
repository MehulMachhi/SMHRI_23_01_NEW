from django.shortcuts import render, redirect
from .models import Appoinment, ChemicalExamination, City, Country, DiffierentialCount, Enquiry , State, UserCompany, Users
from .models import SummaryReport

########################### Appoinment ################################

###################### ADD Report Code ####################

def add_report_appointment(request):
    if request.method == "POST":
        post = Appoinment()
        post.name = request.POST.get('name')
        post.email = request.POST.get('email')
        post.date = request.POST.get('date')
        post.message = request.POST.get('message')
        post.save()
        return render(request, 'add-report-appointment.html')
    else:
        return render(request, 'add-report-appointment.html')

###################### View Report Code ####################

def view_report_appointment(request):
    alldata = Appoinment.objects.all()
    return render(request, 'view-report-appointment.html', {'stu', alldata})

###################### Update Report Code ####################

def update_report_appointment(request):
    update = Appoinment.objects.get(id=id)
    update.save()
    return render(request, 'update-report-appointment.html', {"edit": update})

###################### Delete Report Code ####################

def delete_report_appointment(request):
    delete = Appoinment.objects.get(id=id)
    delete.delete()
    return redirect('/')

########################### Chemicalexamination ################################

###################### ADD Report Code ####################

def add_report_chemicalexamination(request):
    if request.method == "POST":
        post = ChemicalExamination()
        post.chem_exam = request.POST.get('chem_exam')
        post.emp_id = request.POST.get('emp_id')
        post.volume = request.POST.get('volume')
        post.transparency = request.POST.get('transparency')
        post.deposit = request.POST.get('deposit')
        post.colour = request.POST.get('colour')
        post.sp_gravity = request.POST.get('sp_gravity')
        post.ph_reaction = request.POST.get('ph_reaction')
        post.pus_cells = request.POST.get('pus_cells')
        post.rbc = request.POST.get('rbc')
        post.epi_cells = request.POST.get('epi_cells')
        post.casts = request.POST.get('casts')
        post.crystals = request.POST.get('crystals')
        post.bacteria = request.POST.get('bacteria')
        post.yeast_cells = request.POST.get('yeast_cells')
        post.trichomonas = request.POST.get('trichomonas')
        post.amorphous_deposit = request.POST.get('amorphous_deposit')
        post.albumin = request.POST.get('albumin')
        post.sugar = request.POST.get('sugar')
        post.acetone = request.POST.get('acetone')
        post.bile_pigments = request.POST.get('bile_pigments')
        post.bile_salts = request.POST.get('bile_salts')
        post.urobilinogen = request.POST.get('urobilinogen')
        post.save()
        return render(request, 'add_report_chemicalexamination.html')
    else:
        return render(request, 'add_report_chemicalexamination.html')

###################### VIEW Report Code ####################

def view_report_chemicalexamination(request):
    alldata = ChemicalExamination.objects.all()
    return render(request, 'view-report-chemicalexamination.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_chemicalexamination(request):
    update = ChemicalExamination.objects.get(id=id)
    update.save()
    return render(request, 'update-report-chemicalexamination.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_chemicalexamination(request):
    delete = ChemicalExamination.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## City #########################################

###################### ADD Report Code ####################

def add_report_city(request):
    if request.method == "POST":
        post = City()
        post.city = request.POST.get('city')
        post.city_name = request.POST.get('city_name')
        post.state = request.POST.get('state')
        post.save()
        return render(request, 'add-report-city.html')
    else:
        return render(request, 'add-report-city.html')

###################### VIEW Report Code ####################

def view_report_city(request):
    alldata = City.objects.all()
    return render(request, 'view-report-city.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_city(request):
    update = City.objects.get(id=id)
    update.save()
    return render(request, 'update-report-city.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_city(request):
    delete = City.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## Country #########################################

###################### ADD Report Code ####################

def add_report_country(request):
    if request.method == "POST":
        post = Country()
        post.country = request.POST.get('country')
        post.country_name = request.POST.get('country_name')
        post.save()
        return render(request, 'add-report-country.html')
    else:
        return render(request, 'add-report-country.html')

###################### VIEW Report Code ####################

def view_report_country(request):
    alldata = Country.objects.all()
    return render(request, 'view-report-country.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_country(request):
    update = Country.objects.get(id=id)
    update.save()
    return render(request, 'update-report-country.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_country(request):
    delete = Country.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## DiffierentialCount #########################################

###################### ADD Report Code ####################

def add_report_diffierentialcount(request):
    if request.method == "POST":
        post = DiffierentialCount()
        post.diff_count = request.POST.get('diff_count')
        post.emp_id = request.POST.get('emp_id')
        post.neutrophils = request.POST.get('neutrophils')
        post.eosinophil = request.POST.get('eosinophil')
        post.monocytes = request.POST.get('monocytes')
        post.basophil = request.POST.get('basophil')
        post.save()
        return render(request, 'add-report-diffierentialcount.html')
    else:
        return render(request, 'add-report-diffierentialcount.html')

###################### VIEW Report Code #####################

def view_report_diffierentialcount(request):
    alldata = DiffierentialCount.objects.all()
    return render(request, 'view-report-diffierentialcount.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_diffierentialcount(request):
    update = DiffierentialCount.objects.get(id=id)
    update.save()
    return render(request, 'update-report-diffierentialcount.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_diffierentialcount(request):
    delete = DiffierentialCount.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## Enquiry #########################################

###################### ADD Report Code ####################

def add_report_enquiry(request):
    if request.method == "POST":
        post = Enquiry()
        post.name = request.POST.get('name')
        post.email = request.POST.get('email')
        post.phone = request.POST.get('phone')
        post.message = request.POST.get('message')
        post.save()
        return render(request, 'add-report-enquiry.html')
    else:
        return render(request, 'add-report-enquiry.html')

###################### VIEW Report Code ####################

def view_report_enquiry(request):
    alldata = Enquiry.objects.all()
    return render(request, 'view-report-enquiry.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_enquiry(request):
    update = Enquiry.objects.get(id=id)
    update.save()
    return render(request, 'update-report-enquiry.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_enquiry(request):
    delete = Enquiry.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## State #########################################

###################### ADD Report Code ####################

def add_report_state(request):
    if request.method == "POST":
        post = State()
        post.state = request.POST.get('state')
        post.state_name = request.POST.get('state_name')
        post.country = request.POST.get('country')
        post.save()
        return render(request, 'add-report-state.html')
    else:
        return render(request, 'add-report-state.html')

###################### VIEW Report Code ####################

def view_report_state(request):
    alldata = State.objects.all()
    return render(request, 'view-report-state.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_state(request):
    update = State.objects.get(id=id)
    update.save()
    return render(request, 'update-report-state.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_state(request):
    delete = State.objects.get(id=id)
    delete.delete()
    return redirect('/')


######################################## UserCompany #########################################

###################### ADD Report Code ####################

def add_report_usercompany(request):
    if request.method == "POST":
        post = UserCompany()
        post.user_company = request.POST.get('user_company')
        post.user = request.POST.get('user')
        post.company = request.POST.get('company')
        post.save()
        return render(request, 'add-report-usercompany.html')
    else:
        return render(request, 'add-report-usercompany.html')

###################### VIEW Report Code ####################

def view_report_usercompany(request):
    alldata = UserCompany.objects.all()
    return render(request, 'view-report-usercompany.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_usercompany(request):
    update = UserCompany.objects.get(id=id)
    update.save()
    return render(request, 'update-report-usercompany.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_usercompany(request):
    delete = UserCompany.objects.get(id=id)
    delete.delete()
    return redirect('/')

######################################## Users #########################################

###################### ADD Report Code ####################

def add_report_users(request):
    if request.method == "POST":
        post = Users()
        post.email = request.POST.get('email')
        post.first_name = request.POST.get('first_name')
        post.last_name = request.POST.get('last_name')
        post.phone = request.POST.get('phone')
        post.photo = request.POST.get('photo')
        post.role = request.POST.get('role')
        post.password = request.POST.get('password')
        post.last_login = request.POST.get('last_login')
        post.status = request.POST.get('status')
        post.banned_users = request.POST.get('banned_users')
        post.user_com = request.POST.get('user_com')
        post.save()
        return render(request, 'add-report-users.html')
    else:
        return render(request, 'add-report-users.html')

###################### VIEW Report Code ####################


# def view_report_users(request):
#     alldata = Users.objects.all()
#     return render(request, 'view-report-users.html', {'stu', alldata})

###################### UPDATE Report Code ####################

def update_report_users(request):
    update = Users.objects.get(id=id)
    update.save()
    return render(request, 'update-report-users.html', {"edit": update})

###################### DELETE Report Code ####################

def delete_report_users(request):
    delete = Users.objects.get(id=id)
    delete.delete()
    return redirect('/')




##################################################### VIEW Employee/Report Code ############################################


def view_employee_reports(request):
    return render(request, 'emp-reports.html')


def view_summary_reports(request):
    alldata = SummaryReport.objects.all()
    return render(request, 'summary-reports.html', {'stu': alldata})

##################################################### VIEW Employee/Report Code ############################################




# def reports(request):
#     return render(request, 'report.html')


























