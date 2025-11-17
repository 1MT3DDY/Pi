from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Login

def index(request):
    context = {}
    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
            context['usuario'] = usuario
            if usuario.perfil:
                context['perfil_nombre'] = usuario.perfil.nombre
        except Usuario.DoesNotExist:
            pass
    return render(request, 'pagina/index.html', context)

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


def register_view(request):
    """Handle user registration."""
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        contraseña = request.POST.get('contraseña', '').strip()
        confirmar_contraseña = request.POST.get('confirmar_contraseña', '').strip()
        
        # Validations
        if not nombre:
            messages.error(request, 'El nombre de usuario es requerido.')
            return render(request, 'pagina/register.html')
        
        if len(nombre) < 3:
            messages.error(request, 'El nombre de usuario debe tener al menos 3 caracteres.')
            return render(request, 'pagina/register.html')
        
        if len(nombre) > 20:
            messages.error(request, 'El nombre de usuario no puede exceder 20 caracteres.')
            return render(request, 'pagina/register.html')
        
        if not contraseña:
            messages.error(request, 'La contraseña es requerida.')
            return render(request, 'pagina/register.html')
        
        if len(contraseña) < 4:
            messages.error(request, 'La contraseña debe tener al menos 4 caracteres.')
            return render(request, 'pagina/register.html')
        
        if contraseña != confirmar_contraseña:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'pagina/register.html')
        
        # Check if username already exists
        if Usuario.objects.filter(nombre=nombre).exists():
            messages.error(request, 'El nombre de usuario ya está registrado.')
            return render(request, 'pagina/register.html')
        
        # Create new user
        try:
            usuario = Usuario.objects.create(
                nombre=nombre,
                contraseña=contraseña
            )
            messages.success(request, f'¡Registro exitoso! Bienvenido {nombre}. Por favor inicia sesión.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error al registrar el usuario: {str(e)}')
            return render(request, 'pagina/register.html')
    
    return render(request, 'pagina/register.html')


def logout_view(request):
    """Cierra la sesión removiendo la clave 'usuario_id' de la sesión y redirige al índice."""
    try:
        if 'usuario_id' in request.session:
            del request.session['usuario_id']
    except Exception:
        pass
    return redirect('/')
