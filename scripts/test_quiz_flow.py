from django.test import Client
from pagina.models import Usuario, QuizIn
from quiz.models import preguntas

# Ensure user exists
user, created = Usuario.objects.get_or_create(nombre='test_user', defaults={'contraseña': 'test'})

# Ensure there are some preguntas
if preguntas.objects.count() == 0:
    preguntas.objects.create(pregunta='¿Te arriesgas a invertir en acciones?', respuesta_1=0, respuesta_2=5, respuesta_3=10)
    preguntas.objects.create(pregunta='¿Cuál es tu horizonte de inversión?', respuesta_1=0, respuesta_2=5, respuesta_3=10)

client = Client()
session = client.session
session['usuario_id'] = user.id
session.save()

resp = client.get('/quiz/question/0/')
print('GET /quiz/question/0/ ->', resp.status_code)
print(resp.content.decode('utf-8')[:1000])

# Submit answer for question 0 and follow redirect
resp2 = client.post('/quiz/question/0/', {'respuesta': '2'}, follow=True)
print('POST /quiz/question/0/ ->', resp2.status_code)
print('Redirect chain:', [r.status_code for r in resp2.redirect_chain])
print('Final URL content snippet:', resp2.content.decode('utf-8')[:500])
