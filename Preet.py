
from django.shortcuts import *
import http.client
from django.http import JsonResponse
import csv
from csv import *

from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')
def index(request):
    rd=open("C:\\Users\\hp\\Desktop\\data.csv","r")
    x = []
    while True:
        line=rd.readline()
        if line=="":
            break
        data=line.split(",")
        d = []
        d.append(data[0])
        d.append(data[1])
        d.append(data[2])
        d.append(data[3])
        d.append(data[4])
        d.append(data[5])
        x.append(d)
    return JsonResponse(x,safe=False)
@csrf_exempt
def add(request):
    id=request.POST['textbox1']
    name=request.POST['textbox2']
    sal=request.POST['textbox3']
    des=request.POST['textbox4']
    mob=request.POST['textbox5']
    gen=request.POST['textbox6']
    x=[]
    x.append(id)

    x.append(name)

    x.append(sal)

    x.append(des)

    x.append(mob)

    x.append(gen)

    wr = open("C:\\Users\\hp\\Desktop\\data.csv","a",newline='')
    obj=csv.writer(wr)
    obj.writerow(x)


    return HttpResponse("success")


