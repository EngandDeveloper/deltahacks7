from django.shortcuts import render

from .models import Doctor, Patient
from input.models import UserInput
# Create your views here.
def dashboard(request):
    isDoctor = False
    user = request.user
    userDoctor = Doctor.objects.all().filter(user__username__contains=user.username)
    userPatient = Patient.objects.all().filter(user__username__contains=user.username)

    # print(len(userDoctor), len(userPatient))

    if len(userDoctor) != 0:
        isDoctor = True
    elif len(userPatient) != 0:
        isDoctor = False
    else:
        return render(request, 'doctorpatient/registertypes.html')

    if isDoctor:
        patients = Patient.objects.all().filter(doctor__user__username__contains=user.username)
        context = {'patients':patients}
        return render(request, 'doctorpatient/doctordashboard.html', context)
    else:
        #get the last 3 measurement record here as well
        recordList = UserInput.objects.all().filter(user__username__contains=user.username)
        records = []
        if len(recordList) >= 3:
            for i in range(len(recordList)-3,len(recordList)):
                records.append(recordList[i])
        doctorName = userPatient[0].doctor.user.username

        user_data = UserInput.objects.all().filter(user__username__contains=user.username)
        dates = []
        sys = []
        dia = []
        # print(type(user_data[0].current_date))
        for data_point in user_data:
            sys.append(str(data_point.high_blood_pressure))
            dia.append(str(data_point.low_blood_pressure))
            dates.append(str(data_point.current_date)[:10]) 

        context = {'doctorName':doctorName, 'records':records, 'labels' : dates,'dia_data': dia,'sys_data': sys}
        return render(request, 'doctorpatient/patientdashboard.html', context)


def newPatient(request):
    user = request.user
    form = Patient()
    
    if request.method == "POST":
        location = request.POST.get('location')
        doctorName = request.POST.get('doctor')
        doctorObject = Doctor.objects.all().filter(user__username__contains=doctorName)
        doctor = doctorObject[0]
        print("Doctor is:", doctor)
        form = Patient(user = user, location = location, doctor = doctor)
        form.save()
    return render(request, 'users/index.html')

def newDoctor(request):
    user = request.user
    form = Doctor()
    
    if request.method == "POST":
        location = request.POST.get('location')
        medicalID = request.POST.get('medicalID')
        form = Doctor(user = user, location = location, medicalID = medicalID)
        form.save()
    return render(request, 'users/index.html')

def seeUser(request):
    if request.method == "POST":
        user = request.POST.get('patientname')
        userPatient = Patient.objects.all().filter(user__username__contains=user)
        recordList = UserInput.objects.all().filter(user__username__contains=user)
        records = []
        if len(recordList) >= 3:
            for i in range(len(recordList)-3,len(recordList)):
                records.append(recordList[i])
        doctorName = userPatient[0].doctor.user.username

        user_data = UserInput.objects.all().filter(user__username__contains=user)
        dates = []
        sys = []
        dia = []
        # print(type(user_data[0].current_date))
        for data_point in user_data:
            sys.append(str(data_point.high_blood_pressure))
            dia.append(str(data_point.low_blood_pressure))
            dates.append(str(data_point.current_date)[:10]) 

        context = {'doctorName':doctorName, 'records':records, 'labels' : dates,'dia_data': dia,'sys_data': sys}
        return render(request, 'doctorpatient/patientdashboard.html', context)
