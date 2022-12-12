from django.shortcuts import render
from django.http import HttpResponse
from Home.models import PetProduct

def detail(request):
    id=request.GET["id"]
    data=PetProduct.objects.get(id=id)
    total=int(data.price)-(int(data.price*data.discount/100))
    print(data)
    return render(request,"detail.html",{"pro":data,"total":total})
