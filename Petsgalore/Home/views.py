from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def test(request):
    val="php"
    var="lang"
    return render(request,"test.html",{"a":val,"b":var})
    


