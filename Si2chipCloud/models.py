from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

#Temperature measurement class
class TempMeasure(models.Model):
    #temperature = models.CharField(max_length=250, blank=False)
    temperature = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return str(self.temperature)
    #code
#Motion measurement class
class MotionMeasure(models.Model):
    motion = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.motion)
    
    
#humidity measurement class
class HumidityMeasure(models.Model):
    humidity = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.humidity)
    

    
#light intensity measurement class
class LigthIntesityMeasure(models.Model):
    light_intensity = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.light_intensity)

#Camera state acknowledgement
class CameraState(models.Model):
    camera = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.camera)
      
    
#Main gate  state acknowledment class
class MainGateState(models.Model):
    main_gate = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.main_gate)


#AC state acknowledment class
class AcSatte(models.Model):
    air_conditioner = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.air_conditioner)

#TV state acknowlegdement class  
class TvState(models.Model):
    tv_state = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.tv_state)


#Washing Machine ackknowledgement class
class WashingMachineState(models.Model):
    washing_machine = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return str(self.washing_machine)
