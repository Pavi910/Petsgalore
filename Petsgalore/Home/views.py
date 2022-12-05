from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    return render(request,"index.html")

def test(request):
    val="php"
    var="lang"
    return render(request,"test.html",{"a":val,"b":var})

def log(request):
    return render(request,"login.html")

def reg(request):

    return render(request,"register.html")
    
def loginsub(request):
    user=request.GET['Uname']
    pas=request.GET['Pname']
    check=auth.authenticate(username=user,password=pas)
    if check is not None:
        auth.login(request,check)
        return redirect("/")
    else:
        msg="Invalid username and password"
        return render(request,"test.html",{"msg":msg})

def registersub(request):
    uname=request.GET['uname']
    pname=request.GET['pname']
    ename=request.GET['ename']
    fname=request.GET['fname']
    lname=request.GET['lname']
    rpname=request.GET['rpname']
    ucheck=User.objects.filter(username=uname)
    echeck=User.objects.filter(email=ename)
    pcheck=User.objects.filter(password=pname)
    if ucheck:
        msg="Username is already taken"
        return render(request,"test.html",{"msg":msg})

    elif echeck:
        msg="E-Mail is already taken"
        return render(request,"test.html",{"msg":msg})

    elif pname=="" or pname!=rpname:
        msg="Password is incorrect"
        return render(request,"test.html",{"msg":msg})

    else:
        user=User.objects.create_user(username=uname,email=ename,first_name=fname,last_name=lname,password=pname)
        user.save();
        return redirect("/")


