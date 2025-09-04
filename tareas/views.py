from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .models import Tarea
from .forms import TareaForm

def home(request):
    return render(request, 'tareas/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada. ¡Bienvenido!")
            return redirect('tareas')
    else:
        form = UserCreationForm()
    return render(request, 'tareas/signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Has iniciado sesión.")
            return redirect('tareas')
    else:
        form = AuthenticationForm()
    return render(request, 'tareas/signin.html', {'form': form})

def signout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('signin')

def lista_tareas(request):
    tareas = Tarea.objects.filter(owner=request.user, completada=False).order_by('-creada')
    return render(request, 'tareas/tareas.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.owner = request.user
            tarea.save()
            messages.success(request, "Tarea creada.")
            return redirect('tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})

@login_required
def detalles_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, owner=request.user)
    return render(request, 'tareas/detalles_tarea.html', {'tarea': tarea})

@login_required
def actualizar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarea actualizada.")
            return redirect('tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})

@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, owner=request.user)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, "Tarea eliminada.")
        return redirect('tareas')
    return render(request, 'tareas/confirm_delete.html', {'tarea': tarea})


@login_required
def toggle_completada(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, owner=request.user)
    tarea.completada = not tarea.completada
    tarea.save()
    if tarea.completada:
        return redirect('tareas_completadas')
    else:
        return redirect('tareas')



@login_required
def tareas_completadas(request):
    tareas = Tarea.objects.filter(owner=request.user, completada=True).order_by('-creada')
    return render(request, 'tareas/tareas_completadas.html', {'tareas': tareas})