from django.shortcuts import render
from .models import formulario

# Create your views here.
def inicio(request):
    return render(request, 'index.html', {})

def galeria(request):
    return render(request, 'galeria.html', {})

def formulario(request):
    return render(request, 'form.html', {})

def datos(request):
    return render(request, 'datos.html', {})



def Formuladio(request):
    Nombre= request.POST('nombre')
    Apellido= request.POST('apellido')
    Correo= request.POST('correo')
    Producto= request.POST('producto')
    Telefono= request.POST('telefono')
    Direccion= request.POST('direccion')
    Sugerencia= request.POST('sugerencia')
    p=formulario(nombre=Nombre,apellido=Apellido,correo=Correo,producto=producto,telefono=Telefono,direccion=Direccion,sugerencia=Sugerencia)
    p.save()
    return render(request, 'datos.html', {'nombre': Nombre})
