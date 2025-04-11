from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo, esta es la vista de Index Polls.")
    
def results(request, pregunta_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def detail(request, pregunta_is):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)

def vote(request, pregunta_id):
    return HttpResponse("Estas votando en la pregunta %s." % pregunta_id)