from django.shortcuts import render

# Si2chipCloud-TempMeasure views

from .models import TempMeasure
from .forms import TempMeasureForm
# Si2chipCloud MotionMeasure views here.
from .models import MotionMeasure
from .forms import MotionMeasureForm

#Django transaction rollback
from django.db import transaction, DatabaseError
transaction.rollback()
#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#def index(request):
    #return render(request, 'Si2chipCloud/index.html', {})
def home(request):
    
    
    title = 'IoT Si2chip'
    msg='Welcome To Si2chip'

    
    form1 = TempMeasureForm(request.POST)
    form2 = MotionMeasureForm(request.POST)
    context = {
        "title": title,
        "welcome": msg,
        "form1": form1,
        "form2": form2
        
    }
    
    instance1 = form1.save(commit=False)
    instance1.save()
    instance2 = form2.save(commit=False)
    instance2.save()

    queryset = TempMeasure.objects.all().order_by('-timestamp')
    context = {
        "queryset": queryset,
        "form1": form1,
        "form2": form2
    }
    
    return render(request, 'Si2chipCloud/home.html', context)
    
    

