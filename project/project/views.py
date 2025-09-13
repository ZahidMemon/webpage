from django.shortcuts import render
from django.http import HttpResponse
from home.models import Home
from contact.models import Contact

def homePage(request):
    homePage_data=Home.objects.all()

    homePage_data_render={
        'index':homePage_data,
    }
    return render(request,'index.html',homePage_data_render)

def contactPage(request):
    contactPage_data=Contact.objects.all()

    contactPage_data_render={
        'contact':contactPage_data,
    }
    return render(request,'contact.html',contactPage_data_render)