from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse

def index(request):
    response = "<html><body>"
    response += "<h2> Catalogue </h2>"
    response += "<br>Current time is %s" % datetime.datetime.now().time()
    response += "</html></body>"
    return HttpResponse(response)

def search(request, product_name):
    response = "<html><body>"
    response += "<h2> Search </h2>"
    response += "<br>Search details for product named "+product_name+" ..."
    response += "<br>Current time is %s" % datetime.datetime.now().time()
    response += "</html></body>"
    return HttpResponse(response)
