from django.urls import path
from . import views
from clothes_mix import views as core_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria', views.galeria, name='galeria'),
    path('formulario', views.formulario, name='formulario'),
    path('formulario2',views.formulario2,name='formularioRegistro'),
    path('datos', views.datos, name='datos'),
    path('registro/', core_views.signup, name='signup'),
]