from Home.models import PetProduct
from django.conf import settings
from .models import comment
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.core.cache import cache



def detail(request):
    id=request.GET["id"]
    data=PetProduct.objects.get(id=id)
    total=int(data.price)-(int(data.price*data.discount/100))
    print(data)
    if "his" in request.session:
        if id in request.session["his"]:
            request.session["his"].remove(id)
            request.session["his"].insert(0,id)
        else:
            request.session["his"].insert(0,id)
        
        if len(request.session["his"])>4:
            request.session["his"].pop()
        print(request.session["his"])
        prop=PetProduct.objects.filter(id__in=request.session["his"])
        print(prop)
        request.session.modified=True
        return render(request,"detail.html",{"pro":data,"total":total,"abc":prop})
                
    else:
        print("Hello")
        request.session["his"]=[id]
        return render(request,"detail.html",{"pro":data,"total":total})
    

def click(request):
    user=request.POST['user']
    id=request.POST['id']
    com=request.POST['com']
    cmt=comment.objects.create(cmnt=com,name=user,pro_id=id)
    cmt.save();
    return redirect("/product/?id="+id)

def detail2(request):
    id=request.GET["id"]
    if cache.get(id):
        print("data from cache")
        data=cache.get(id)
    else:
        print("data from database")
        data=PetProduct.objects.get(id=id)
        cache.set(id,data)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    return render(request,"detail.html",{"pro":data,"total":total})

def email(request):
    email_from=settings.EMAIL_HOST_USER
    email_to=["kukku9102@gmail.com"]
    subject="Hello"
    message="Hello World"
    send_mail=(subject,message,email_from,email_to)
    return render(request,"test.html")