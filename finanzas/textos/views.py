from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse, Http404
RESPUESTAS_FIJAS = {
    1: {
        'pregunta': "¿Es importante registrar ingresos y gastos?", 
        'respuesta': "La clave es el presupuesto: asigna un nombre a cada euro antes de gastarlo.",
    },
    2: {
        'pregunta': "¿Que papel tiene el habito y disciplina?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    3: {
        'pregunta': "¿Que es la regla 50/30/20?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    4: {
        'pregunta': "¿Ahorro a corto o largo plazo?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    5: {
        'pregunta': "¿Es importante el fondo de emergencia en ahorro?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    6: {
        'pregunta': "¿Ahorrar en efectivo o en instrumentos financieros?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    7: {
        'pregunta': "¿Como tiene que ser un buen lugar para guardar ahorro?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    8: {
        'pregunta': "¿Como debería empezar?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    9: {
        'pregunta': "¿Que importancia tiene la fijacion de objetivos?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    10: {
        'pregunta': "¿Que es el fondo de emergencia?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    11: {
        'pregunta': "¿Que efecto tiene la inflacion?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    12: {
        'pregunta': "¿Como funciona el interes compuesto?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    13: {
        'pregunta': "¿Que es el riesgo y retorno?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    14: {
        'pregunta': "¿Que es el horizonte de inversion?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    15: {
        'pregunta': "¿Que es diversificaion?",
        'respuesta': "Prioriza deudas de alto interés (tarjetas). Luego, enfócate en el ahorro.",
    },
    # recuerdo pa tontos:
    # 3: {'pregunta': "¿Qué hago con un ingreso extra?", 'respuesta': "nadota we"
    16: {
        'pregunta': "¿Como debería empezar?",
        'respuesta': "Es la práctica de distribuir tus inversiones entre diferentes activos para reducir el riesgo.",
    },
}

def textos_view(request):
    
    preguntas_ids = range(1, 17) 
    
    contexto = {
        'titulo_pagina': 'Preguntas y Respuestas',
        'preguntas_ids': preguntas_ids
    }
    return render(request, 'textos/index.html', contexto)

# Vista de Detalle (Para la respuesta bonita)
def pregunta_detalle(request, pregunta_id):
    pregunta_id = int(pregunta_id)
    if pregunta_id not in RESPUESTAS_FIJAS:
        raise Http404("La pregunta solicitada no existe")
    datos_pregunta = RESPUESTAS_FIJAS[pregunta_id]
    

    contexto = {
        'titulo_pagina': datos_pregunta['pregunta'],
        'respuesta_bonita': datos_pregunta['respuesta']
    }
    return render(request, 'textos/preguntas_detalle.html', contexto)