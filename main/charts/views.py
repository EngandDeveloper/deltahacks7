from django.shortcuts import render
from input.models import UserInput
# Create your views here.

def line_chart(request):
    dates = ['February 1','February 2','February 3','February 4']
    sys = [120,110,125,110]
    dia = [75,80,90,70]
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

    print(user_data[0].current_date)
    # queryset = Sys.objects.order_by('-date') query data from here
    # for sys in queryset:
    #     labels.append(sys.date)
    #     data.append(sys.value)

    return render(request, 'charts/line-chart.html', {
        'labels' : dates,
        'dia_data': dia,
        'sys_data': sys
    })