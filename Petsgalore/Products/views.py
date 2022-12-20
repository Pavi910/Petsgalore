from django.shortcuts import render,redirect
from django.http import HttpResponse
from Home.models import PetProduct
from Products.models import comment

def detail(request):
    id=request.GET["id"]
    data=PetProduct.objects.get(id=id)
    total=int(data.price)-(int(data.price*data.discount/100))
    print(data)
    res=render(request,"detail.html",{"pro":data,"total":total})
    res.set_cookie("pr",data.price)
    return res

def click(request):
    user=request.POST['user']
    id=request.POST['id']
    com=request.POST['com']
    cmt=comment.objects.create(cmnt=com,name=user,pro_id=id)
    cmt.save();
    return redirect("/product/?id="+id)