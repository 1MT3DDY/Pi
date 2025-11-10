from django.shortcuts import render
# La funcion le falta las condiciones del tipo de usuario: Ahorrador, Equilibrado , Gastador. Por ahora dejare esta funcion como base 
def vista_calculadora(request):
    
    contexto = {}

    if request.method == "POST":
        
        try:
            # Obtener los datos del formulario (salario y gastos fijos)
            ingresos = float(request.POST.get('ingresos', 0))
            
            # Los gastos fijos que vienen del formulario
            gasto_arriendo = float(request.POST.get('gasto_arriendo', 0))
            gasto_servicios = float(request.POST.get('gasto_servicios', 0)) 
            gasto_educacion = float(request.POST.get('gasto_educacion', 0))
            gasto_otros = float(request.POST.get('gasto_otros', 0))

            #Los sumamos 
            total_gastos_fijos = gasto_arriendo + gasto_servicios + gasto_educacion + gasto_otros
            
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

            if presupuesto <= 15000:
                mensaje = "¡Números Rojos!!! Tienes un déficit de ${:,.0f}.".format(presupuesto)
                status_color = "red"

            elif (proporcion_gastos > 0.6): # si los gastos fijos superan el 60% de los ingresos
                mensaje = "¡Cuidado! Numeros Amarillos. Tus gastos fijos son muy altos. Te quedan ${:,.0f}.".format(presupuesto)
                status_color = "yellow"

            else:
                mensaje = "¡Numeros Verdes! Tu presupuesto estu saludable. Te quedan ${:,.0f}.".format(presupuesto)
                status_color = "green"

            # la distribucion del presupuesto en bases a las categorias 
            if presupuesto > 0:
                contexto['distribucion'] = {
                    'mercaderia': presupuesto * 0.40, 
                    'salud': presupuesto * 0.20,
                    'ahorro': presupuesto * 0.20,
                    'inversion': presupuesto * 0.10,
                    'chucherias': presupuesto * 0.10, # estos porcentajes seran ajustados a futuro, por ahora estos seran de base 
                }
            
            # pasamos los resultados al contexto para la plantilla
            contexto['ingresos'] = ingresos
            contexto['total_gastos_fijos'] = total_gastos_fijos
            contexto['presupuesto'] = presupuesto
            contexto['status_mensaje'] = mensaje
            contexto['status_color'] = status_color
            contexto['form_data'] = request.POST 

        except Exception as e:
            contexto['error'] = "Error en los datos: {}. Asegurate de ingresar solo numeros.".format(e) 

    # renderizamos la plantilla con el contexto 
    return render(request, 'calculadora/index.html', contexto) 
