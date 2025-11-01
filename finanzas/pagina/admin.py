from django.contrib import admin

# Register your models here.

from .models import Usuario, QuizIn, Login


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'perfil')
	search_fields = ('nombre',)


@admin.register(QuizIn)
class QuizInAdmin(admin.ModelAdmin):
	list_display = ('id', 'id_us', 'puntaje', 'tipo_perfil')
	search_fields = ('id_us__nombre',)


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre_usuario', 'fecha_login')
	search_fields = ('nombre_usuario',)

