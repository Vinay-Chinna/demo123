from django.shortcuts import render
from django.http import HttpResponse

import datetime


# Create your views here.

def home(request):
    ct = str(datetime.datetime.now())
    return HttpResponse('<h1>Hi Welcome to Index Page  .... </h1>' +   ct)