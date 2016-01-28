from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^si2chip_cloud/', views.index, name='index'),
]