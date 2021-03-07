from django.shortcuts import render

from .models import Doctor, Patient
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
        doctorName = userPatient[0].doctor.user.username
        context = {'doctorName':doctorName}
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