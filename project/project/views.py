from django.shortcuts import render
from django.http import HttpResponse
from home.models import Home

def homePage(request):
    homePage_data=Home.objects.all()

    homePage_data_render={
        'index':homePage_data,
    }
    return render(request,'index.html',homePage_data_render)