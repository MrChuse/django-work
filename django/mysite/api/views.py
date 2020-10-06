import os
import json

from .config import ROOT_DIR

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    f = []
    for el in os.listdir(ROOT_DIR):
        if os.path.isfile(ROOT_DIR + '/' + el):
            time = os.path.getmtime(ROOT_DIR + '/' + el)
            f.append({'name':el, 'type':'file', 'time':time})
    d = {'data':f}
    return HttpResponse(json.dumps(d))