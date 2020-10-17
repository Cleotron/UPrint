from django.urls import path
from uprintapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpymes', views.consultaPyme, name='fpyme'),

]



