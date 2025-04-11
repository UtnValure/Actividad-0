from django.shortcuts import render
from django.http import HttpResponse
from .models import pregunta
from django.template import loader

def index(request):
    ultimas_preguntas = pregunta.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"ultimas_preguntas": ultimas_preguntas}
    return HttpResponse(template.render(context, request))
    
def results(request, pregunta_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def detail(request, pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)

def vote(request, pregunta_id):
    return HttpResponse("Estas votando en la pregunta %s." % pregunta_id)