from django.contrib import admin

# Register your models here.
from .models import TempMeasure
from .forms import TempMeasureForm

from .models import MotionMeasure
from .forms import MotionMeasureForm

from .models import HumidityMeasure

from .models import LigthIntesityMeasure

from .models import CameraState

from .models import MainGateState

from .models import AcSatte

from .models import TvState

from .models import WashingMachineState


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
admin.site.register(HumidityMeasure)
admin.site.register(LigthIntesityMeasure)
admin.site.register(CameraState)
admin.site.register(MainGateState)
admin.site.register(AcSatte)
admin.site.register(TvState)
admin.site.register(WashingMachineState)