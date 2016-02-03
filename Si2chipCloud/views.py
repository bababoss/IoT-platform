from django.shortcuts import render

# Create your views here. Si2chipCloud
from django.shortcuts import render
from .forms import TempMeasureForm
# Create your views here.


#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#def index(request):
    #return render(request, 'Si2chipCloud/index.html', {})
def home(request):
    
    title = 'IoT Si2chip'
    msg='Welcome To Si2chip'
    form = TempMeasureForm(request.POST)
    context = {
        "title": title,
        "welcome": msg,
        "form": form
    }
    
    instance = form.save(commit=False)
    instance.save()
    
    
    
    
    return render(request, 'Si2chipCloud/home.html', context)
    

