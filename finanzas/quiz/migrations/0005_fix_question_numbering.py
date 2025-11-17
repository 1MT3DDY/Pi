from django.db import migrations


def fix_question_numbering(apps, schema_editor):
    """Update question text to be numbered 1-10 instead of 4-13."""
    Preguntas = apps.get_model('quiz', 'preguntas')
    question_map = {
        4: 'Pregunta 1',
        5: 'Pregunta 2',
        6: 'Pregunta 3',
        7: 'Pregunta 4',
        8: 'Pregunta 5',
        9: 'Pregunta 6',
        10: 'Pregunta 7',
        11: 'Pregunta 8',
        12: 'Pregunta 9',
        13: 'Pregunta 10',
    }
    for qid, new_text in question_map.items():
        Preguntas.objects.filter(id_pregunta=qid).update(pregunta=new_text)


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_populate_questions'),
    ]

    operations = [
        migrations.RunPython(fix_question_numbering),
    ]
