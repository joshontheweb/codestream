import datetime
from django.shortcuts import render

def home(request):
    template_vars = {
        'datetime': datetime.datetime.now()
    }
    return render(request, 'home.html', template_vars) 