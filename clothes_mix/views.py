from django.shortcuts import render
from .models import Formulario


# Create your views here.
def inicio(request):
    return render(request, 'index.html', {})


def galeria(request):
    return render(request, 'galeria.html', {})


def formulario(request):
    return render(request, 'form.html', {})


def datos(request):
    return render(request, 'datos.html', {})


def formulario2(request):
    nombre = request.POST['Nombre']
    apellido = request.POST['apellido']
    correo = request.POST['correo']
    producto = request.POST['producto']
    telefono = request.POST['telefono']
    direccion = request.POST['direccion']
    sugerencia = request.POST['sugerencia']
    p = Formulario(nombre=nombre, apellido=apellido, correo=correo, producto=producto, telefono=telefono,
                   direccion=direccion, sugerencia=sugerencia)
    p.save()
    return render(request, 'registrogood.html', {'Nombre': nombre})
