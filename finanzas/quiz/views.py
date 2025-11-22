from django.shortcuts import render, redirect
from django.contrib import messages
from .models import preguntas
from pagina.models import Usuario, QuizIn, Perfil


def usuario_puede_tomar_quiz(request):
    if 'usuario_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión para realizar el quiz')
        return None, redirect('login')
    try:
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado. Inicia sesión nuevamente.')
        return None, redirect('login')
    existing_quizzes = QuizIn.objects.filter(id_us=usuario)
    if existing_quizzes.exists():
        messages.info(request, 'Ya tienes un quiz asociado. No puedes volver a completarlo.')
        return None, redirect('index')
    return usuario, None

def quiz_landing(request):
    if 'usuario_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión para ver el quiz')
        return redirect('login')
    
    try:
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
    except Usuario.DoesNotExist:
        return redirect('login')


    tiene_quiz = QuizIn.objects.filter(id_us=usuario).exists()
    
    context = {
        'tiene_quiz': tiene_quiz,
        'usuario': usuario
    }

    return render(request, 'quiz/quiz.html', context)

def quiz_start(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
        
    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    # Logitic de la estructureishon
    # Si el usuario ya tiene un quiz y decide comenzar de nuevo, borramos lo anterior
    QuizIn.objects.filter(id_us=usuario).delete() # Borra el registro del quiz anterior
    usuario.perfil = None  # Quita el perfil asociado ahora
    usuario.score = 0      # Reinicia el puntaje del usuario
    usuario.save()         # Guarda los cambios en la fokin base waaaaa

    q_ids = list(preguntas.objects.values_list('id_pregunta', flat=True).order_by('id_pregunta'))
    if not q_ids:
        messages.error(request, 'No hay preguntas disponibles.')
        return redirect('index')
        
    request.session['quiz_qids'] = q_ids
    request.session['quiz_answers'] = {}
    request.session['quiz_score'] = 0
    request.session.modified = True
    
    return redirect('quiz_question', idx=0)


def quiz_question(request, idx):
    """Show a single question by index and handle saving the selected answer into the session."""
    usuario, redirect_resp = usuario_puede_tomar_quiz(request)
    if redirect_resp:
        return redirect_resp

    qids = request.session.get('quiz_qids') #qids = question ids porsiaca
    if qids is None:
        return redirect('quiz')

    total = len(qids)
    if idx < 0 or idx >= total:
        return redirect('quiz')

    qid = qids[idx]
    try:
        pregunta = preguntas.objects.get(id_pregunta=qid)
    except preguntas.DoesNotExist:
        messages.error(request, 'Pregunta no encontrada.')
        return redirect('index')

    # On POST save the answer and move to next or submit
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta not in ('1', '2', '3'):
            messages.error(request, 'Selecciona una opción válida.')
            return redirect('quiz_question', idx=idx)

        answers = request.session.get('quiz_answers', {})
        answers[str(qid)] = respuesta
        request.session['quiz_answers'] = answers
        
        # Compute score increment based on answer
        if respuesta == '1':
            score_add = pregunta.respuesta_1
        elif respuesta == '2':
            score_add = pregunta.respuesta_2
        else:  # respuesta == '3'
            score_add = pregunta.respuesta_3
        
        # Update usuario.score in database
        usuario.score += score_add
        usuario.save()
        
        # Keep score in session for display
        request.session['quiz_score'] = usuario.score
        request.session.modified = True

        # If there is a next question, go there; otherwise submit
        if idx + 1 < total:
            return redirect('quiz_question', idx=idx + 1)
        else:
            return redirect('quiz_submit')

    # GET: render single question
    answers = request.session.get('quiz_answers', {})
    selected = answers.get(str(qid))
    current_score = request.session.get('quiz_score', 0)
    progress_percent = int(((idx + 1) / total) * 100) if total > 0 else 0
    context = {
        'pregunta': pregunta,
        'idx': idx,
        'total': total,
        'selected': selected,
        'current_score': current_score,
        'progress_percent': progress_percent,
    }
    return render(request, 'quiz/question.html', context)


def quiz_submit(request):
    """Create QuizIn record, assign user profile based on puntaje, and show results."""
    usuario, redirect_resp = usuario_puede_tomar_quiz(request)
    if redirect_resp:
        return redirect_resp

    qids = request.session.get('quiz_qids')
    answers = request.session.get('quiz_answers', {})
    if not qids:
        messages.error(request, 'No hay respuestas para procesar o la sesión expiró.')
        return redirect('quiz')

    puntaje_total = 0
    for qid in qids:
        try:
            preg = preguntas.objects.get(id_pregunta=qid)
        except preguntas.DoesNotExist:
            continue
        resp = answers.get(str(qid))
        if resp == '1':
            puntaje_total += preg.respuesta_1
        elif resp == '2':
            puntaje_total += preg.respuesta_2
        elif resp == '3':
            puntaje_total += preg.respuesta_3

    # Crea el registro del quiz
    QuizIn.objects.create(
        id_us=usuario,
        puntaje=puntaje_total
    )

    # Asignar perfil basándose en el puntaje
    if puntaje_total <= 33:
        perfil_id = 1
        tipo_perfil = 'conservador'
    elif puntaje_total <= 66:
        perfil_id = 2
        tipo_perfil = 'normal'
    else:
        perfil_id = 3
        tipo_perfil = 'arriesgado'

    try:
        perfil = Perfil.objects.get(id=perfil_id)
        usuario.perfil = perfil
        usuario.save()
    except Perfil.DoesNotExist:
        messages.warning(request, f'Perfil {perfil_id} no encontrado en la base de datos.')

    for k in ('quiz_qids', 'quiz_answers', 'quiz_score'):
        if k in request.session:
            del request.session[k]
    request.session.modified = True

    messages.success(request, f'¡Quiz completado! Tu perfil es: {tipo_perfil.capitalize()}. Tu puntuación acumulada es: {usuario.score}')
    return redirect('index')