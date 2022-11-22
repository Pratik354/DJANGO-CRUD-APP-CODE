from urllib import request
from webbrowser import GenericBrowser
from django.shortcuts import render,HttpResponseRedirect
from MYAPP.models import APP

def home(request):
    if request.method=='POST':
        FIRST_NAME=request.POST.get('first')
        LAST_NAME=request.POST.get('last')
        EMAIL=request.POST.get('mail')
        NUMBER=request.POST.get('num')
        AGE=request.POST.get('age')
        GENDER=request.POST.get('gender')
        DATA=APP(FIRST_NAME=FIRST_NAME,LAST_NAME=LAST_NAME,EMAIL=EMAIL,NUMBER=NUMBER,AGE=AGE,GENDER=GENDER)
        DATA.save()
    return render(request,'index.html')

def show(request):
    data=APP.objects.all()
    return render(request,'show.html',{'data':data})

def edit(request):
    ID=request.GET['id']
    for data in APP.objects.filter(ID=ID):
        FIRST_NAME=data.FIRST_NAME
        LAST_NAME=data.LAST_NAME
        EMAIL=data.EMAIL
        NUMBER=data.NUMBER
        AGE=data.AGE
        GENDER=data.GENDER
    return render(request,'edit.html',{'ID':ID,'FIRST_NAME':FIRST_NAME,'LAST_NAME':LAST_NAME,'EMAIL':EMAIL,'NUMBER':NUMBER,'AGE':AGE,'GENDER':GENDER})

def update(request):
    if request.method=='POST':
        ID=request.POST['id']
        FIRST_NAME=request.POST['first']
        LAST_NAME=request.POST['last']
        EMAIL=request.POST['mail']
        NUMBER=request.POST['num']
        AGE=request.POST['age']
        GENDER=request.POST['gender']
        APP.objects.filter(ID=ID).update(FIRST_NAME=FIRST_NAME,LAST_NAME=LAST_NAME,EMAIL=EMAIL,NUMBER=NUMBER,AGE=AGE,GENDER=GENDER)
        return HttpResponseRedirect('show')

def delete(request):
    ID=request.GET['id']
    APP.objects.filter(ID=ID).delete()
    return HttpResponseRedirect('show')
