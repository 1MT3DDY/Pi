# Generated manually to handle Perfil creation and data population

import django.db.models.deletion
from django.db import migrations, models


def create_perfiles(apps, schema_editor):
    """Create the 3 default profile records."""
    Perfil = apps.get_model('pagina', 'Perfil')
    Perfil.objects.create(id=1, nombre='Conservador', descripcion='Perfil conservador')
    Perfil.objects.create(id=2, nombre='Normal', descripcion='Perfil normal')
    Perfil.objects.create(id=3, nombre='Arriesgado', descripcion='Perfil arriesgado')


def reverse_perfiles(apps, schema_editor):
    """Delete the 3 default profile records."""
    Perfil = apps.get_model('pagina', 'Perfil')
    Perfil.objects.filter(id__in=[1, 2, 3]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_alter_usuario_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.RunPython(create_perfiles, reverse_perfiles),
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to='pagina.perfil'),
        ),
    ]
