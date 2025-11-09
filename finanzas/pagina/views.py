from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Login

def index(request):
    return render(request, 'pagina/index.html')

def videos_view(request):
    return render(request, 'pagina/videos.html')


# NO LO TOQUEN 4 horas de mi vida se fueron en esto
def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        
        try:
            # ta pa verificar el login
            usuario = Usuario.objects.get(nombre=nombre, contraseña=contraseña)
            
            login = Login(nombre_usuario=nombre, contraseña_usuario=contraseña)
            login.save()
            
            # guarda el id del user
            request.session['usuario_id'] = usuario.id
            
            # si login == True => you are going to brazil
            return redirect('/')  
            
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos')
            
    return render(request, 'pagina/login.html')


def logout_view(request):
    """Cierra la sesión removiendo la clave 'usuario_id' de la sesión y redirige al índice."""
    try:
        if 'usuario_id' in request.session:
            del request.session['usuario_id']
    except Exception:
        pass
    return redirect('/')
