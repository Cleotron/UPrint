from django.urls import path
from clientesapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpymes', views.consultaPyme, name='fpyme'),
    path('huellapymes', views.huellaPyme, name='hpyme'),

]



