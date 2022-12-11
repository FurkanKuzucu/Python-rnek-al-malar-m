from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import book
import datetime

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
def save(request):
    return render(request, 'pages/save.html')
def search (request):
    return render (request,'pages/search.html')
def addbook(request):
    if request.method=="GET":
        return redirect("/search")
    else:
        title=request.POST.get("nam")
        typ=request.POST.get("type")
        categ=request.POST.get("categ")
        newBook= book(title =title,typ=typ,categr=categ)
        newBook.save(book)
        return redirect ("/search")
def findbook(request):
    
    
    if request.method=="GET":
        return redirect("pages/save.html")
    else:
        titlee=request.POST.get("names")
        books=book.objects.all()
        howm=len(books)
        for j in range(1,howm):
            box=[]
            
            for i in books:
                if i.title==titlee:
                    box.append(i)
            return render(request,"pages/save.html",{"book":box})
def delt(request,id):
    bookd=book.objects.filter(id=id).first()
    
    bookd.delete()
    return render (request,'pages/save.html')
def datetime(request):
    e = datetime.datetime.now()
    b="Bugünün tarihi:  = %s/%s/%s" % (e.day, e.month, e.year)
    return render(request,"pages/index.html",{"datetime":b})