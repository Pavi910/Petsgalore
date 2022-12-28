from django.contrib import admin
from django.urls import path
from.import views
from. import feed

urlpatterns = [
    path("",views.index,name="home page"),
    path("login/",views.log,name="login page"),
    path("register/",views.reg,name="register page"),
    path("logout/",views.logout,name="logout page"),
    path("otp/",views.otp,name="otppage"),
    path("feed/",feed.latestproduct()),

]