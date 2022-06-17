from django.http import HttpResponse
from django.shortcuts import render
from DesafioAPP.models import *
from django.http import HttpResponse
from django.template import loader, Context
# Create your views here.

def familia (self):
    familiar1 = Familia(nombre= "Erick", apellido= "Sandoval", edad = "25", fechainscripcion = "2022-06-15")
    familiar2 = Familia(nombre= "Maria", apellido= "Garrido", edad = "64", fechainscripcion = "2022-06-15")
    familiar3 = Familia(nombre= "Yasna", apellido= "Sandoval", edad = "33", fechainscripcion = "2022-06-15")
    familiar1.save()
    familiar2.save()
    familiar3.save()

    nombres = (f"{familiar1.nombre}, {familiar2.nombre} y {familiar3.nombre}")
    apellidos = (f"{familiar1.apellido}, {familiar2.apellido} y {familiar3.apellido}")
    edades = (f"{familiar1.edad}, {familiar2.edad} y {familiar3.edad}")
    fecha = (familiar1.fechainscripcion)

    familiatexto = {"nombres": nombres, "apellidos": apellidos, "edades": edades, "fecha": fecha}

    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render(familiatexto)

    return HttpResponse (documento)