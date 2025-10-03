from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Estoy en el index de los polls")

def detail(request, question_id):
    return HttpResponse("Estas viendo la pregunta %s." % question_id)

def results(request, question_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s." % question_id)

