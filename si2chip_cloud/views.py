from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#def index(request):
#   return HttpResponse("hello suresh")

def index(request):
    return render(request, 'si2chip_cloud/index.html', {})