from django.shortcuts import render, redirect
from .models import UserInput


# Create your views here.
def user_input_screen(request):
    if not request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        if request.POST.get("input_data"):
            blood_pressure = request.POST.get("blood_pressure")
            date_recorded = request.POST.get("date_recorded")
            current_user = request.user

            print(blood_pressure)
            print(date_recorded)
            print(current_user)

            return redirect("/")

    return render(request, "input/user_input.html")