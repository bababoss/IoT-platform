
from django import forms
from .models import TempMeasure
from .models import MotionMeasure

class  TempMeasureForm(forms.ModelForm):
    class Meta:
        model = TempMeasure
        fields = ['temperature']
        #code
    
class  MotionMeasureForm(forms.ModelForm):
    class Meta:
        model = MotionMeasure
        fields = ['motion']
        #code