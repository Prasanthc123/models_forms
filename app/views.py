from django.shortcuts import render
from  app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            QLTO=Topic.objects.all()
            d1={'Topic':QLTO}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            QWTO=Webpage.objects.all()
            d1={'Webpage':QWTO}
            return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)