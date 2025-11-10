from django.shortcuts import render, redirect
from django.contrib import messages
from .models import preguntas
from pagina.models import Usuario, QuizIn

def quiz_view(request):
    # debug: print session for local troubleshooting (can be removed later)
    print("Session:", request.session.items())
    if 'usuario_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión para realizar el quiz')
        return redirect('login')
    # comprobar que el usuario existe
    try:
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado. Inicia sesión nuevamente.')
        return redirect('login')
    # comprobar si el usuario ya tiene quizzes asociados (no permitir si ya hay alguno)
    existing_quizzes = QuizIn.objects.filter(id_us=usuario)
    if existing_quizzes.exists():
        messages.info(request, 'Ya tienes un quiz asociado. No puedes volver a completarlo.')
        return redirect('index')
    if request.method == 'POST':
        # Obtener todas las preguntas
        todas_preguntas = preguntas.objects.all()
        puntaje_total = 0

        # Calcular puntaje total
        for pregunta in todas_preguntas:
            respuesta = request.POST.get(f'pregunta_{pregunta.id_pregunta}')
            if respuesta:
                if respuesta == '1':
                    puntaje_total += pregunta.respuesta_1
                elif respuesta == '2':
                    puntaje_total += pregunta.respuesta_2
                elif respuesta == '3':
                    puntaje_total += pregunta.respuesta_3

        # Crear el registro de QuizIn asociado al usuario
        quiz_in = QuizIn.objects.create(
            id_us=usuario,
            puntaje=puntaje_total
        )

        # Determinar el tipo de perfil para mostrar al usuario
        if puntaje_total <= 30:
            tipo_perfil = 'conservador'
        elif puntaje_total <= 60:
            tipo_perfil = 'normal'
        else:
            tipo_perfil = 'arriesgado'

        messages.success(request, f'¡Quiz completado! Tu perfil es: {tipo_perfil.capitalize()}')
        return redirect('index')
    
    # GET request - mostrar el formulario
    # GET request - mostrar el formulario
    context = {
        'preguntas': preguntas.objects.all(),
        'can_take_quiz': True,
    }
    return render(request, 'quiz/quiz_form.html', context)