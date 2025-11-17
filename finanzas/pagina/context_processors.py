from .models import Usuario


def usuario_context(request):
    """Context processor que agrega el nombre de usuario y el tipo de perfil
    a todas las plantillas si el usuario está logueado (guardado en sesión).
    Variables añadidas:
      - usuario_nombre
      - usuario_tipo (nombre del perfil)
    """
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return {}
    try:
        usuario = Usuario.objects.select_related('perfil').get(id=usuario_id)
    except Usuario.DoesNotExist:
        return {}

    tipo = None
    if usuario.perfil:
        tipo = usuario.perfil.nombre

    return {
        'usuario_nombre': usuario.nombre,
        'usuario_tipo': tipo,
    }
