from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import commentbox
from . forms import commentboxForm


def index(request):
    return render(request,'faunasea/homepage.html')

def about(request):
    return render(request,'faunasea/about.html')

def contact(request):
    return render(request,'faunasea/contact.html')

def info(request):
    if request.method=="POST":
        form = commentboxForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"faunasea/info.html")
        else:
            return render(request,"faunasea/errorpage.html")

    else:
        return render(request,"faunasea/errorpage.html")

