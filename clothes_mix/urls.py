from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria', views.galeria, name='galeria'),
    path('formulario', views.formulario, name='formulario'),
    path('formulario2',views.formulario2,name='formularioRegistro'),
    path('datos', views.datos, name='datos'),
]