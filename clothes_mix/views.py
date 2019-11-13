from django.shortcuts import render, redirect
from .models import Formulario
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm


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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})