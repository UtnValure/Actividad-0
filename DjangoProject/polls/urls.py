from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name='detalle'),
    path("<int:pk>/resultados/", views.ResultsView.as_view(), name="resultados"),
    path("<int:pregunta_id>/votos/", views.vote, name="votos"),
]