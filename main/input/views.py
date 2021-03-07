from django.shortcuts import render, redirect
from .models import UserInput


# Create your views here.
def user_input_screen(request):
    if not request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        if request.POST.get("input_data"):
            high_blood_pressure = request.POST.get("high_blood_pressure")
            low_blood_pressure = request.POST.get("low_blood_pressure")
            date_recorded = request.POST.get("date_recorded")
            current_user = request.user

            print(high_blood_pressure)
            print(low_blood_pressure)
            print(date_recorded)
            print(current_user)

            # If user does not input a date, use current date
            if (not date_recorded):
                user_input = UserInput.objects.create(high_blood_pressure=high_blood_pressure,
                                                      low_blood_pressure=low_blood_pressure,
                                                      user=current_user)

            else:
                user_input = UserInput.objects.create(current_date=date_recorded,
                                                      high_blood_pressure=high_blood_pressure,
                                                      low_blood_pressure=low_blood_pressure,
                                                      user=current_user)
            user_input.save()

            user= request.user
            user_data = UserInput.objects.all().filter(user__username__contains=user.username)
            dates = []
            sys = []
            dia = []
            print(type(user_data[0].current_date))
            for data_point in user_data:
                sys.append(str(data_point.high_blood_pressure))
                dia.append(str(data_point.low_blood_pressure))
                dates.append(str(data_point.current_date)[:10])
            return render(request, "doctorpatient/patientdashboard.html", 
            {'labels' : dates,
            'dia_data': dia,
            'sys_data': sys})

    return render(request, "input/user_input.html")