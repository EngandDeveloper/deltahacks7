from django.shortcuts import render, redirect
from .models import UserInput

# Create your views here.
def user_input_screen(request):
    #user_data = UserInput.objects.get(id=id)
    #if not request.user.is_authenticated or user_data not in request.user.author.all():
    #    return redirect("/")

    if request.method == "POST":
        if request.POST.get("input_data"):
            blood_pressure = request.POST.get("blood_pressure")
            date_recorded = request.POST.get("date_recorded")


            print(blood_pressure)
            print(date_recorded)

            return redirect("/")

    return render(request, "input/user_input.html")