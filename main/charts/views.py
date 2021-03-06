from django.shortcuts import render

# Create your views here.

def line_chart(request):
    dates = ['February 1','February 2','February 3','February 4']
    dia = [75,80,90,70]
    # queryset = Sys.objects.order_by('-date') query data from here
    # for sys in queryset:
    #     labels.append(sys.date)
    #     data.append(sys.value)

    return render(request, 'line-chart.html', {
        'labels' : dates,
        'data': dia,
    })