from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'si2chip_cloud/index.html', {})