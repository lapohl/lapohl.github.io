from django.db import models
from datetime import date
from django.utils import timezone
from django.forms import ModelForm

class Task(models.Model):
  task = models.CharField(max_length=200)
  hole = models.CharField(max_length=200)
  frequency_days = models.IntegerField(default=2)
  next_due_date = models.DateField(default=timezone.now)

class Log(models.Model):
  task = models.CharField(max_length=200)
  hole = models.CharField(max_length=200)
  #equipment = models.CharField(max_length=200)
  #hours = models.IntegerField(default=0)
  date_completed = models.DateTimeField(default='2001-01-01 11:11:11')

class Equipment(models.Model):
  equipment_name = models.CharField(max_length=200)
  hours_used = models.IntegerField(default=0)

