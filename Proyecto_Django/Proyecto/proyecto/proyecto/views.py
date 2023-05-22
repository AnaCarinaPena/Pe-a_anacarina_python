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
        'cel' : "Cel: ",
        'celular' : "(33)-1801-3455",
        'cor' :"Correo: ",
        'correo' : "carinape@gmail.com",
        'dom' : "Domicilio:",
        'domicilio' : "Av.La Cima 3500, Col. Colinas del Rey",
        'sex' : "Sexo:",
        'sexo' : "Femenino",
        'obj' : "Objetivo:",
        'objetivo' : "Implementar todos mis conocimientos en la empresa",
        'sal_esp' : "Salario Esperado:",
        'salario_esperado' : "$20,000 - $30,000"}
    
        skills ={
            'toma_de_decisiones' : 'Toma de Decisiones',
            'Trabajo_en_Equipo' : 'Trabajo en Equipo',
            'Poder_de_Negociasion': 'Poder de Negociacion',
            'Pensamiento_Critico': 'Pensamiento Critico'
        }

        jobs ={
            "lugar_trabajo1" : "Hewlett Packard Enterprise", "año_inicio" : 2021, "año_fin" :2022, "posicion" : "Import Export Analyst",
            "lugar_trabajo2" : "Ferrero de Mexico S.A de C.V" , "año_inicio" : 2018, "año_fin" :2021, "posicion" : "Import Policy and Compliance Analyst",
        }

       
        return render (request, self.template_name, datos) 
        #return render (request, self.template_name ,datos, skills, jobs)
    