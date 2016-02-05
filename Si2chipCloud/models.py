from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.
class TempMeasure(models.Model):
    #temperature = models.CharField(max_length=250, blank=False)
    temperature = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return str(self.temperature)
    #code

class MotionMeasure(models.Model):
    motion = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return str(self.motion)
    #code
