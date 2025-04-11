from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pregunta_id>/", views.detail, name='detalle'),
    path("<int:pregunta_id>/resultados/", views.results, name="resultados"),
    path("<int:pregunta_id>/votos/", views.vote, name="votos"),
]