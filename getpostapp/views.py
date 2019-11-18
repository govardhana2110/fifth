from django.shortcuts import render
from django.http import HttpResponse
def getadd(request):
    return render(request,'get.html')
def postadd(request):
    return render(request,'post.html')
def add(request):
    if request.method=="GET":
        x=int(request.GET['t1'])
        y=int(request.GET['t2'])
        z=x+y
        return HttpResponse("<html><body bgcolor=green>sum is :"+str(z)+"</body></html>")
    else:
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        z = x + y
        return HttpResponse("<html><body bgcolor=green>sum is :"+str(z)+"</body></html>")


