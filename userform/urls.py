#from django.contrib import admin
from django.urls import path
from . import views

app_name='userform'

urlpatterns = [
    path('',views.userinput, name='userinput'),
    path('read/',views.Read,name='read'),
]
