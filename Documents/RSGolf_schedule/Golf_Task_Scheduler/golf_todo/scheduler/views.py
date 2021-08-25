from django.shortcuts import render
from scheduler.models import Task
from scheduler.models import Log
import pandas as pd
from golf_todo.forms import TaskForm
import requests
import json
import time
import urllib.request
from json import dumps
from datetime import date, timedelta, datetime

def getForecast():
  hourly_forecast = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/329381?apikey=MR2VVK6jYPJ7ZvS5c9R1tA7HszjSt7xM&details=true"
  temps = []
  humidity = []
  time = []
  precipitation = []
  rain = []
  prec_hr_data = []

  with urllib.request.urlopen(hourly_forecast) as hourly_forecast:
    data = json.loads(hourly_forecast.read().decode())
    for hour_data in data:
      temps.append(hour_data["Temperature"]["Value"])
      humidity.append(hour_data["RelativeHumidity"])
      time.append(hour_data["DateTime"])
      precipitation.append(hour_data["PrecipitationProbability"])
      rain.append(hour_data["Rain"]["Value"])
  
  hours = []

  for idx, timestamp in enumerate(time):
    timestamp = timestamp.split("T")[1].split("-")[0].split(":")[0]
    hours.append(int(timestamp))

  context = {
    'temps': temps,
    'humidity': humidity,
    'rain': rain,
    'None': 'None',
    'time': hours,
    'prec_hourly': dumps(precipitation),
  }

  return(context)

def getCurrentWeather():
  current_weather = "http://dataservice.accuweather.com/currentconditions/v1/329381?apikey=MR2VVK6jYPJ7ZvS5c9R1tA7HszjSt7xM&details=true"
  with urllib.request.urlopen(current_weather) as current_weather:
    data = json.loads(current_weather.read().decode())

    context = {
      'temp': data[0]['Temperature']['Imperial']['Value'],
      'humidity': data[0]['RelativeHumidity'],
      'prec': data[0]['PrecipitationType'],

    }
  return(context)

def home(request):
  #setting initial weather API call time: 8/22/21 10AM
  time_0 = datetime(year=2021, month=8, day=22, hour=10, minute=0)
  check_time = datetime.now() 
  
  if (check_time > (time_0 + timedelta(hour=1))):
    time_0 = check_time

    hourly_forecast_dict = getForecast()
    current_weather_dict = getCurrentWeather()
    
  if request.method == 'POST':
    form = TaskForm(request.POST)

    if (isinstance(int(request.POST['id']),int)):
      task_to_update = Task.objects.get(id=int(request.POST['id']))
      task_to_update.next_due_date = timedelta(days=task_to_update.frequency_days) + today
      task_to_update.save()

      new_entry = Log.objects.create(
        task = task_to_update.task,
        hole = task_to_update.hole,
        date_completed = now,
      )
      new_entry.save()

  else:
    form = TaskForm()
    
    log_entries = Log.objects.all()
    tasks = Task.objects.all()
    dun_time = today - timedelta(days=2)

    context = {
      'hour_temps': hourly_forecast_dict['temps'],
      'humidity': hourly_forecast_dict['humidity'],
      'prec_hourly': hourly_forecast_dict['prec_hourly'],
      'cur_temp': current_weather_dict['temp'],
      'cur_hum': current_weather_dict['humidity'],
      'prec': current_weather_dict['prec'],
      'time': hourly_forecast_dict['time'],
      'tasks': tasks,
      'today': today,
      'form': form,
      'logs': log_entries,
      'dun_time': dun_time,
    
    }
  
    return render(request, 'index.html', context=context)

  def log_entry(request):
    return render(request, 'log_entry.html')

  def edit_task(request):
    form = TaskForm()
    tasks = Task.objects.all()
    task_types = Task.objects.order_by().values('task').distinct()
    context = {
      'tasks': tasks,
      'task_types': task_types,
      'form': form,
    }

    return render(request, 'view_edit_tasks.html', context=context)

def delete_task(request, id):
  task_to_delete = Task.objects.get(id=id)
  task_to_delete.delete()
  tasks = Task.objects.all()
  context = {
    'tasks': tasks,
  }
  return render(request, 'view_edit_tasks.html', context=context)