from django.shortcuts import render
from pagina.models import Usuario  
from django.shortcuts import redirect 
import random 

def vista_calculadora(request):
    
    mensaje_recomendado = {
        "1": { #Ahorrador 
            "red" : ["Un buen fondo de emergencia es clave para tu tranquilidad. Te recomendamos ver nuestros <a href='/videos/'>Videos sobre Ahorro</a>.", 
                     "¡Alerta!. Tu perfíl ahorrador no deberia estar en deficit. Lee nuestra guía <a href='/textos/pregunta/1/'>sobre registro de gastos</a>.", 
                     "Un perfil conservador debe tener <a href='/textos/pregunta/5/'>su Fondo de Emergencia</a> intacto. Enfócate en recuperarlo."],

            "yellow" : ["Mantener la disciplina es fundamental. Revisa nuestros <a href='/textos/pregunta/2/'>consejos sobre hábitos</a>.",
                    "Ahorrar es bueno, pero tu liquidez es baja. Revisa <a href='/textos/pregunta/5/'>el tamaño de tu Fondo de Emergencia</a> para tener un colchón cómodo."], 

            "green" : ["Como perfil Conservador, el ahorro es tu mejor aliado. ¿Sabías que registrar tus gastos es el primer paso? Aprende más en nuestra <a href='/textos/pregunta/1/'>Guía de Ahorro</a>.", 
                       "¿Conoces la regla 50/30/20? Es perfecta para perfiles conservadores. <a href='/textos/pregunta/3/'>Léela aquí</a>.",
                       "Proteger tu dinero de la inflación es vital. Aprende <a href='/textos/pregunta/11/'>aquí</a>.",
                       "Ya superaste el ahorro. Es momento de proteger tu capital: revisa si <a href='/textos/pregunta/6/'>ahorrar en instrumentos financieros</a> te conviene más que el efectivo."]
        }
        , 
        "2": { #Normal 
            "red" : ["Considera crear un <a href='/textos/pregunta/5/'>plan de ahorro para emergencias</a> futuras.", 
                     "Evalúa tus hábitos de gasto y busca áreas donde puedas reducir costos. Mira nuestra guía para <a href='/textos/pregunta/8/'>empezar a ahorrar</a>.", 
                     ],

            "yellow" : ["Un perfil balanceado sabe la diferencia entre ahorro e inversión. <a href='/textos/'>Descubre más en nuestros recursos</a>.", 
                        "Estás cerca del verde. Empieza a investigar sobre <a href='/textos/pregunta/13/'>Riesgo y Retorno</a> antes de invertir."
                        "Considera ajustar tu presupuesto para mejorar tu salud financiera. Revisa la <a href='/textos/pregunta/3/'>Regla 50/30/20</a>."], 

            "green" : ["Para tu perfil Normal, balancear es clave. ¿Conoces la regla 50/30/20? <a href='/textos/pregunta/3/'>Léela aquí</a>.", 
                       "Vimos que tu presupuesto está saludable. ¿Qué tal dar el siguiente paso? Aprende sobre el interés compuesto en nuestros <a href='/videos/'>Videos de Inversión</a>.",
                       "El interés compuesto es tu mejor amigo. <a href='/textos/pregunta/12/'>Lee cómo funciona</a> y sácale provecho a tu presupuesto.",
                       "¿Listo para invertir? Aprende sobre <a href='/textos/pregunta/13/'>Riesgo y Retorno</a> primero."]
        }
        ,
        "3": { #Arriesgado 
            "red" : ["¡No pongas todos los huevos en la misma canasta! Revisa nuestros <a href='/videos/'>Videos de Inversión</a> para aprender a diversificar.", 
                     "Considera buscar asesoría financiera para mejorar tu situación. Revisa nuestra guía sobre <a href='/textos/pregunta/14/'>errores comunes</a>.", 
                     "Evita endeudarte más y enfócate en estabilizar tus finanzas."], 

            "yellow" : ["La diversificación es tu escudo. <a href='/textos/pregunta/15/'>Aprende más aquí</a>.", 
                        "Busca formas de aumentar tus ingresos para mejorar tu situación financiera.",
                        "La falta de control te está costando dinero. Revisa tus <a href='/textos/pregunta/2/'>hábitos de gasto</a> y busca formas de aumentar tu margen. Evita la tentación.", 
                        "Evita los errores de principiante. <a href='/textos/pregunta/14/'>Lee nuestra guía</a> sobre qué no hacer."], 

            "green" : ["Como perfil Arriesgado, te gusta ver crecer tu dinero. ¿Entiendes bien la relación entre <a href='/textos/pregunta/13/'>Riesgo y Retorno</a>?.", 
                    "El interés compuesto es tu mejor amigo. <a href='/textos/pregunta/12/'>Lee cómo funciona</a> y sácale provecho a tu presupuesto.", 
                    "Tu presupuesto está en forma para el crecimiento. Sigue monitoreando tus finanzas y no olvides que la paciencia es la mejor herramienta del inversionista <a href='/textos/pregunta/12/'>Interés Compuesto</a>.",
                    "Tu estilo requiere mitigación de riesgo. Revisa el valor de la <a href='/textos/pregunta/15/'>Diversificación</a>. No tomes decisiones impulsivas, sino estratégicas."]
        } 
    }

    contexto = {}

    if 'usuario_id' not in request.session: 
        return redirect('login') 

    if request.method == "POST":
        
        try:
            # Obtener los datos del formulario (salario y gastos fijos)
            ingresos = float(request.POST.get('ingresos', 0))
            
            # Los gastos fijos que vienen del formulario
            gasto_arriendo = float(request.POST.get('gasto_arriendo', 0))
            gasto_servicios = float(request.POST.get('gasto_servicios', 0)) 
            gasto_educacion = float(request.POST.get('gasto_educacion', 0))
            gasto_transporte = float(request.POST.get('gasto_transporte', 0)) 
            gasto_otros = float(request.POST.get('gasto_otros', 0))

            #Los sumamos 
            total_gastos_fijos = gasto_arriendo + gasto_servicios + gasto_educacion + gasto_transporte + gasto_otros
            
            # definimos el presupuesto 
            presupuesto = ingresos - total_gastos_fijos
            
            mensaje = ""
            # Lógica para el ESTADO (Verde, Amarillo, Rojo) ayuda de IA
            status_color = ""
            
            # calculamos la proporcion de gastos fijos sobre ingersos
            if ingresos > 0:
                proporcion_gastos = total_gastos_fijos / ingresos

            # evitamos division por cero 
            else:
                proporcion_gastos = 0

            u = Usuario.objects.get(id=request.session['usuario_id']) 
            contexto['perfil_id'] = u.perfil_id  

            if presupuesto <= 15000:
                mensaje = "¡Números Rojos! Tienes un déficit de ${:,.0f}.".format(presupuesto)
                status_color = "red"
    
            elif (proporcion_gastos > 0.6): # si los gastos fijos superan el 60% de los ingresos
                mensaje = "¡Cuidado! Numeros Amarillos. Tus gastos fijos son muy altos. Te quedan ${:,.0f}.".format(presupuesto)
                status_color = "yellow"

            else:
                mensaje = "¡Numeros Verdes! Tu presupuesto esta saludable. Te quedan ${:,.0f}.".format(presupuesto)
                status_color = "green"

            contexto['mensaje_recomendado'] = random.choice(mensaje_recomendado[str(u.perfil_id)][status_color])

            # la distribucion del presupuesto en bases a las categorias 
            if presupuesto > 0:

                if u.perfil_id == 1 : #Ahorrador
                    contexto['distribucion'] = {
                        'mercaderia': presupuesto * 0.30, 
                        'salud': presupuesto * 0.15,
                        'ahorro': presupuesto * 0.15,
                        'inversion': presupuesto * 0.05,
                        'transporte': presupuesto * 0.05,
                        'otros': presupuesto * 0.30,  
                    }

                elif u.perfil_id == 2 : #Normal 
                    contexto['distribucion'] = {
                        'mercaderia': presupuesto * 0.30, 
                        'salud': presupuesto * 0.15,
                        'ahorro': presupuesto * 0.10,
                        'inversion': presupuesto * 0.10,
                        'transporte': presupuesto * 0.05,
                        'otros': presupuesto * 0.30,
                    }
                
                elif u.perfil_id == 3 : #Arriesgado  
                    contexto['distribucion'] = {
                        'mercaderia': presupuesto * 0.30, 
                        'salud': presupuesto * 0.15,
                        'ahorro': presupuesto * 0.05,
                        'inversion': presupuesto * 0.15,
                        'transporte': presupuesto * 0.05,
                        'otros': presupuesto * 0.30, 
                }
                else:  
                    contexto['error'] = " Por favor realize el quiz."

            contexto['ingresos'] = ingresos
            contexto['total_gastos_fijos'] = total_gastos_fijos
            contexto['presupuesto'] = presupuesto
            contexto['status_mensaje'] = mensaje
            contexto['status_color'] = status_color
            contexto['form_data'] = request.POST 

        except Exception as e:
            contexto['error'] = "Error en los datos: {}. Asegurate de ingresar solo numeros.".format(e) 

  
    return render(request, 'calculadora/index.html', contexto) 
