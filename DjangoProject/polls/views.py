from django.shortcuts import render, get_object_or_404
from .models import pregunta
from django.template import loader

def index(request):
    ultimas_preguntas = pregunta.objects.order_by("-pub_date")[:5]
    context = {"ultimas_preguntas": ultimas_preguntas}
    return render(request, "polls/index.html", context)
    # render usa ( request, plantilla, diccionario opcional)
    
def results(request, pregunta_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def detail(request, pregunta_id):
    preg = get_object_or_404(pregunta, pk=pregunta_id)
    return render(request, "polls/detail.html", {"pregunta": preg})

def vote(request, pregunta_id):
    return HttpResponse("Estas votando en la pregunta %s." % pregunta_id)