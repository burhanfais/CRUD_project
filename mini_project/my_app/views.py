from django.shortcuts import redirect,render
from .models import Member

# Create your views here.
def index (request):
    mbr=Member.objects.all()
    return render(request,'index.html',{'mbr':mbr})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['first']
    z=request.POST['first']
    mbr=Member(firstname=x,lastname=y,country=z)
    mbr.save()
    return redirect("/")

def delete(request,id):
    mbr=Member.objects.get(id=id)
    mbr.delete()
    return redirect("/")

def update(request,id):
    mbr=Member.objects.get(id=id)
    return render(request,'update.html',{'mbr':mbr})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mbr=Member.objects.get(id=id)
    mbr.firstname=x
    mbr.lastname=y
    mbr.country=z
    mbr.save()
    return redirect("/")