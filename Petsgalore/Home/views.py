from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from.models import PetProduct
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    data=PetProduct.objects.all()
    if "pass" in request.COOKIES and "pr" in request.COOKIES:
        a=request.COOKIES["pass"]
        b=request.COOKIES["pr"]
        return render(request,"index.html",{"pro":data,"cook":a,"pri":b})
    else:
        return render(request,"index.html",{"pro":data})
   

def test(request):
    val="php"
    var="lang"
    return render(request,"test.html",{"a":val,"b":var})

def log(request):
    if request.method=="POST":
        user=request.POST['Uname']
        pas=request.POST['Pname']
        check=auth.authenticate(username=user,password=pas)
        if check is not None:
            auth.login(request,check)
            rep=redirect("/")
            rep.set_cookie("pass",pas)
            return rep
        else:
            msg="Invalid username and password"
            return render(request,"login.html",{"msg":msg})
            
    else:
        return render(request,"login.html")
def reg(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pname=request.POST['pname']
        ename=request.POST['ename']
        fname=request.POST['fname']
        lname=request.POST['lname']
        rpname=request.POST['rpname']
        ucheck=User.objects.filter(username=uname)
        echeck=User.objects.filter(email=ename)
        if ucheck:
            msg="Username is already taken"
            return render(request,"register.html",{"msg":msg})

        elif echeck:
            msg="E-Mail is already taken"
            return render(request,"register.html",{"msg":msg})

        elif pname=="" or pname!=rpname:
            msg="Password is incorrect"
            return render(request,"register.html",{"msg":msg})

        else:
            rep=render(request,"otp.html")
            rep.set_cookie("pass",pname)
            rep.set_cookie("user",uname)
            rep.set_cookie("first",fname)
            rep.set_cookie("last",lname)
            rep.set_cookie("email",ename)
            send_mail("otp validation","your otp is 1234",settings.EMAIL_HOST_USER,[ename,])
            return rep
            #user=User.objects.create_user(username=uname,email=ename,first_name=fname,last_name=lname,password=pname)
            #user.save();
            
            
    else:
        return render(request,"register.html")    

    
def loginsub(request):
    user=request.POST['Uname']
    pas=request.POST['Pname']
    check=auth.authenticate(username=user,password=pas)
    if check is not None:
        auth.login(request,check)
        return redirect("/")
    else:
        msg="Invalid username and password"
        return render(request,"test.html",{"msg":msg})

def logout(request):
    auth.logout(request)
    resp=redirect("/")
    resp.delete_cookie("pass")
    resp.delete_cookie("pr")
    return resp

def detail(request):
    return render(request,"detail.html",{{id}})

def otp(request):

    if request.method=="POST":
        otp=request.POST["oname"]
       
        if otp=="1234":
           username=request.COOKIES["user"]
           password=request.COOKIES["pass"]
           firstname=request.COOKIES["first"]
           lastname=request.COOKIES["last"]
           email=request.COOKIES["email"]
           user=User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
           user.save();
           return redirect("/")
            
            
        else:
            
            return render(request,"otp.html")

    else:
        return render(request,"otp.html")

