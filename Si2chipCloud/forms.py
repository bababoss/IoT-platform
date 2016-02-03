
from django import forms
from .models import TempMeasure

class  TempMeasureForm(forms.ModelForm):
    class Meta:
        model = TempMeasure
        fields = ['temperature']
        #code
    
    #code
