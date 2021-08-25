from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from . import views
from django.conf.urls import url



urlpatterns = [
  path('', views.home, name='home'),
  path('index.html', views.home, name='home'),
  path('log_entry.html', views.log_entry, name='log_entry'),
  path('view_edit_tasks.html', views.edit_task, name='edit_task'),
]