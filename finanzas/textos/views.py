from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.safestring import mark_safe
RESPUESTAS_FIJAS = {
    1: {
        'pregunta': "¿Es importante registrar ingresos y gastos?", 
        'respuesta': """<br><p>Registrar ingresos y gastos es uno de los pasos más fundamentales cuando una persona empieza su camino hacia el ahorro.
La razón es simple: no se puede controlar lo que no se conoce.</p>
<br>
<p>Muchas personas creen que no pueden ahorrar porque “no les alcanza” o porque “ganan poco”. Sin embargo, cuando realmente se ponen a registrar todo lo que gastan durante el mes, se dan cuenta de que una parte importante de su dinero se va en pequeñas compras, impulsivas o automáticas, que muchas veces pasan desapercibidas: una bebida, un delivery, un café, snacks, recargas, aplicaciones, caprichos pequeños, etc. Ese gasto, aunque parezca mínimo, acumulado mes a mes puede impedir ahorrar.</p>
<br>
Registrar ingresos y gastos permite 3 cosas clave:<br>


<br>
1. TOMAR CONCIENCIA DE TU SITUACION REAL<br><br>

<p>La mayoría de las personas vive con una impresión de cuánto gasta, no con una cifra real.
Cuando anotas todo descubres cuáles son tus gastos inevitables (transporte, comida, cuentas). Y cuáles son gastos hormiga (pequeños gastos diarios que parecen inofensivos). Ese reconocimiento inicial suele ser impactante y genera un cambio de mentalidad:
“Ah, no es que no pueda ahorrar, es que no sabía en qué se me estaba yendo el dinero.” </p>
<br>
2. ORDENAR PRIORIDADES
<br><br>
Cuando ves tus gastos frente a tus ojos, puedes preguntarte:<br><br>

> ¿Este gasto era realmente necesario?<br>

> ¿Me aporta algo?<br>

> ¿Podría haber elegido una alternativa más económica?<br><br>

A veces lo que falta no es dinero, sino orden.<br><br>



3. TOMAR DECISIONES PARA MEJORAR<br><br>

Una vez que sabes cuánto entra y cuánto sale, puedes:<br><br>

> Ajustar gastos innecesarios<br> 

> Crear un plan realista de ahorro, aunque sea pequeño,<br>

> Evitar endeudarte,<br>

Y avanzar hacia metas concretas (un viaje, estudios, independencia, etc.).<br>

Registrar no es para limitarte, es para empoderarte.
<br><br>
¿Cómo se puede registrar de forma práctica?<br>

No necesitas algo complejo. Puedes usar:<br><br>

> Una libreta → Escribir cada gasto diario.<br>

> Una planilla Excel / Google Sheets → Más orden visual.<br><br>

Apps gratuitas como:<br>

> Notion<br>

> Mobills<br>

> Fintonic<br>

> Spendee<br>

> Monefy<br><br>

Lo importante no es la herramienta, sino la constancia.""",
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
        'respuesta_bonita': mark_safe(datos_pregunta['respuesta'])
    }
    return render(request, 'textos/preguntas_detalle.html', contexto)