from django.contrib import admin

# Register your models here.
from .forms import TempMeasureForm
from .models import TempMeasure
from .models import MotionSensor

class TempMeasureAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timestamp"]
    forms = TempMeasure
    #class Meta:
        #model = TempMeasure
        #code
    



admin.site.register(TempMeasure, TempMeasureAdmin)
admin.site.register(MotionSensor)