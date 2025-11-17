from django.db import migrations, models


def create_or_update_questions(apps, schema_editor):
    Preguntas = apps.get_model('quiz', 'preguntas')

    data = {
        4: (
            "Guardo un 10% de inmediato y hago un presupuesto estricto para que sobre lo más posible.",
            "Pago el arriendo/estancia, compro la comida, separo para la locomoción y veo cuánto me queda para el mes.",
            "Pienso en las salidas, \"carretes\" o esa ropa que vi",
        ),
        5: (
            "Traigo mi comida preparada en casa todos los días, sin excepción. Es más barato.",
            "Llevo comida de casa (en un táper) la mayoría de los días, pero me doy un gusto una vez por semana",
            "Casi siempre compro almuerzo o snacks en los casinos o locales cercanos.",
        ),
        6: (
            "Prefiero quedarme en mi casa/pensión para descansar o viajar a ver a mi familia para ahorrar.",
            "Planifico un viaje, cotizo buses y hostales para que sea entretenido pero no tan caro.",
            "Un \"paseo\" con amigos a la playa o al sur, sin escatimar en gastos.",
        ),
        7: (
            "Ni siquiera me detengo a mirar; si no estaba en mi lista, no me interesa.",
            "Me gustan, pero si no las necesito, es un gasto, no un ahorro. No las compro.",
            "¡Es una ganga! No la puedo dejar pasar, las compro.",
        ),
        8: (
            "Sí, registro hasta el gasto más pequeño. Sé en qué se va cada peso.",
            "Sí, uso una app o un Excel para mis gastos grandes y revisar a fin de mes.",
            "No realmente. Más o menos sé cuánto gasto, pero no llevo la cuenta.",
        ),
        9: (
            "Excelente. Lo ahorro todo para el próximo mes o para los materiales del siguiente semestre.",
            "Bien. Guardo una parte y la otra la uso para darme un gusto (ej. un delivery rico).",
            "¡Perfecto! Lo gasto en ese videojuego, zapatillas o en el \"carrete\" del fin de semana.",
        ),
        10: (
            "Me apego estrictamente a la lista y compro marcas propias para ahorrar.",
            "Llevo una lista, pero soy flexible si veo una buena oferta o un antojo.",
            "Compro lo que se me antoja y las marcas que me gustan.",
        ),
        11: (
            "Busco tutoriales para arreglarlo yo mismo o le pido ayuda a un amigo. Comprar uno nuevo es el último recurso.",
            "Qué mal. Lo llevo al servicio técnico y uso mi fondo de emergencia para arreglarlo.",
            "Me frustro. Miro altiro cómo sacar el último modelo en cuotas.",
        ),
        12: (
            "Cada peso ahorrado hoy es tranquilidad para mañana.",
            "Hay que equilibrar. Disfrutar ahora, pero también guardar para el futuro.",
            "Para eso estudio/trabajo, merezco mis gustos.",
        ),
        13: (
            "Tu piensas en el futuro y decides no comer, pero tambien te ahorras la plata extra y decides solo tomar micro a pesar de llegar mas tarde.",
            "Eliges no comer y tomar el metro y luego el colectivo para poder descansar antes.",
            "Comes y sacas dinero extra para poder costearte el viaje.",
        ),
    }

    question_number = 1
    for qid, (o1, o2, o3) in data.items():
        obj, created = Preguntas.objects.update_or_create(
            id_pregunta=qid,
            defaults={
                'pregunta': f'Pregunta {question_number}',
                'opcion_1': o1,
                'opcion_2': o2,
                'opcion_3': o3,
                'respuesta_1': 0,
                'respuesta_2': 5,
                'respuesta_3': 10,
            }
        )
        question_number += 1


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_preguntas_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='opcion_1',
            field=models.CharField(default='', max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='opcion_2',
            field=models.CharField(default='', max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='opcion_3',
            field=models.CharField(default='', max_length=500, blank=True),
        ),
        migrations.RunPython(create_or_update_questions),
    ]
