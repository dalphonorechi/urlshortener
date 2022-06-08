import imp
from multiprocessing import context
from re import template
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from . import urlchecker
from .models import UrlObj

@csrf_exempt
def index(request):
    template = loader.get_template('index.html')
    # t = request.POST["url"]
    
    # exists = urlchecker.check_url(t)
    # if exists:
    #     save_url(t)
    #     return HttpResponse(f'The url {t} was shortened.')
    # else:
    #     return HttpResponse("Check url! It is invalid.")
    return HttpResponse(template.render())

@csrf_exempt
def shorten(request):
    template = loader.get_template('shortened.html')
    t = request.POST["url"]
    
    exists = urlchecker.check_url(t)
    response = ""
    if exists:
        save_url(t)
        response = f'The url {t} was shortened.'
    else:
        response = "Check the url! It is invalid."

    context = {
        "response":response,
        "you":"hello"
    }
    
    print(response)
    return HttpResponse(template.render(context))
    
def allurls(request):
     k = list(UrlObj.objects.values())
     template = loader.get_template("allurls.html")
     context = {
         "listurls":k,
         "request":request
     }
     return HttpResponse(template.render(context))   

def get_url(request,id):
    try:
        url = UrlObj.objects.filter(id=id).values()[0]
        # return HttpResponse(url["original_url"])
        return redirect(url["original_url"])
    except:
        return HttpResponse("Id does not exist")
def delete_all(request):
    del_url = UrlObj.objects.all().delete()
    return HttpResponse(del_url)


def save_url(url):
    new_url = UrlObj(original_url=url)
    new_url.save();