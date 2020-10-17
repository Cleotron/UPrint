from django.urls import path
from uprintapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calcula-tu-huella', views.formulario, name='form'),
    path('formpymes', views.consultaPyme, name='fpyme'),

]



