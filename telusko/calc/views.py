from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

# crreating function name as home as we did in urls.py we kept name as home
def home(request):
    ##now = datetime.datetime.now()
    ##htmldata = "<html><h1>It is now %s.</h1></html>" % now
    #return HttpResponse(htmldata)
    return render(request,'home.html',{'name':'Mythrayee'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1+val2
    return render(request,'result.html',{'result': res})