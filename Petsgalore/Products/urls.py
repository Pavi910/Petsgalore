from django.contrib import admin
from django.urls import path
from. import views
from Products import views

urlpatterns = [
     path("",views.detail),
     path("select/",views.click,name="testpage")
]