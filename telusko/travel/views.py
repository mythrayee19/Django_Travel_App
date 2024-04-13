from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination() 
    dest1.name = "CHENNAI"
    dest1.desc = "vantharai vazhaveikum chennai"
    dest.price = 700
    return render(request,'index.html',{'dest1':dest1})

