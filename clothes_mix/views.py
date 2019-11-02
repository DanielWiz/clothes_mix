from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html', {})

def galeria(request):
    return render(request, 'galeria.html', {})

def formulario(request):
    return render(request, 'form.html', {})

def datos(request):
    return render(request, 'datos.html', {})



