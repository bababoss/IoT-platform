from django.contrib import admin

# Register your models here.
from .models import TempMeasure
from .forms import TempMeasureForm

from .models import MotionMeasure
from .forms import MotionMeasureForm

class TempMeasureAdmin(admin.ModelAdmin):
    list_display = ["temperature","timestamp"]
    forms = TempMeasure
    #class Meta:
        #model = TempMeasure
        #code

class MotionMeasureAdmin(admin.ModelAdmin):
    list_display = ["motion","timestamp"]
    forms = MotionMeasure
    #class Meta:
        #model = TempMeasure
        #code
    



admin.site.register(TempMeasure, TempMeasureAdmin)
admin.site.register(MotionMeasure, MotionMeasureAdmin)