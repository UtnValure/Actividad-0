from django.shortcuts import render, get_object_or_404
from .models import pregunta, opcion
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    ultimas_preguntas = pregunta.objects.order_by("-pub_date")[:5]
    context = {"ultimas_preguntas": ultimas_preguntas}
    return render(request, "polls/index.html", context)
    # render usa ( request, plantilla, diccionario opcional)
    
def results(request, pregunta_id):
    preg= get_object_or_404(pregunta, pk=pregunta_id)
    return render(request, "polls/results.html", {"pregunta": preg})

def detail(request, pregunta_id):
    preg = get_object_or_404(pregunta, pk=pregunta_id)
    return render(request, "polls/detail.html", {"pregunta": preg})

def vote(request, pregunta_id):
    preg= get_object_or_404(pregunta, pk=pregunta_id)
    try:
        seleccion = preg.opcion_set.get(pk=request.POST["opcion"])
    except (KeyError, opcion.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "pregunta": preg,
                "error_message": "No seleccionaste ninguna opción.",
            },
        )
    else:
        seleccion.votos = F("votos") + 1
        seleccion.save()
        return HttpResponseRedirect(reverse("polls:resultados", args=(preg.id,)))