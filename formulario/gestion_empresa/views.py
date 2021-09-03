from django.db.models.fields import DateTimeCheckMixin
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Persona
from .forms import EmpleadoForm

def inicio(request):
    
    #ahora=datetime.datetime.now()
    personas=Persona.objects.all() 
    contexto={'personas':personas}
    #contexto={'ahora_t':ahora}
    return render (request,'index.html',contexto)


def crearempleado(request):

    if request.method == 'GET':
        form=EmpleadoForm()
        contexto={'form':form}
    else: 
        form=EmpleadoForm(request.POST)
        contexto={'form':form}
        if form.is_valid():
            form.save()
            return redirect('index') 
    return render(request,'crear_empleado.html',contexto)


def editarempleado(request,id):

    persona=Persona.objects.get(id = id)
    if request.method == 'GET':
        form=EmpleadoForm(instance = persona)
        contexto={'form':form }
    else: 
        form=EmpleadoForm(request.POST, instance = persona)
        contexto={'form':form}
        if form.is_valid():
            form.save()
            return redirect('index')
    return render (request,'clear_empleado.html',contexto)


def eliminarempleado(request,id):

    persona=Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')
