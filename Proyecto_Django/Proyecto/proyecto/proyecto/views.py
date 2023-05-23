from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render

import json


def index(request):
    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name ="index.html"
    

    def post(self,request):
        return render(request)
    
    
    def get(self,request):
        datos = {
        'nomb' : "Nombre: ",
        'nombre' : "Ana Carina",
        'primer_apellido' : "Peña",
        'segundo_apellido' : "Lopez",
        'fecha_n' : "Fecha nacimiento: ",
        'fecha_nacimiento' : "30/04/1994",
        'cel' : "Cel: ",
        'celular' : "(33)-1801-3455",
        'cor' :"Correo: ",
        'correo' : "carinape@gmail.com",
        'dom' : "Domicilio:",
        'domicilio' : "Av.La Cima 3500, Col. Colinas del Rey, Zapopan Jalisco",
        'sex' : "Sexo:",
        'sexo' : "Femenino",
        'obj' : "Objetivo:",
        'objetivo' : "Planificar, gestionar y desarrollar las operaciones comerciales en el mercado internacional ",
        'sal_esp' : "Salario Esperado:",
        'salario_esperado' : "$20,000 - $30,000"}
    

        skills ={
            'toma_de_decisiones' : 'Toma de Decisiones',
            'Trabajo_en_Equipo' : 'Trabajo en Equipo',
            'Poder_de_Negociasion': 'Poder de Negociacion',
            'Pensamiento_Critico': 'Pensamiento Critico'
        }

        jobs ={
            "lugar_trabajo1" : "Hewlett Packard Enterprise", "año_inicio_1" : 2021, "año_fin_1" :2022, "puesto_1" : "Import Export Analyst",
            "lugar_trabajo2" : "Ferrero de Mexico S.A de C.V" , "año_inicio_2" : 2018, "año_fin_2" :2021, "puesto_2" : "Import Policy and Compliance Analyst",
        }
        Dic_Master={**datos, **skills, **jobs}

        return render (request, self.template_name, Dic_Master) 
       
    