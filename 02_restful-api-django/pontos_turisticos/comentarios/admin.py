from django.contrib import admin
from .models import Comentario

from .actions import aprova_comentarios, reprova_comentarios


class ComentarioAdmin(admin.ModelAdmin):
    """
    Actions personalizadas para o Django Admin (ações em massa)
    """
    list_display = ['usuario', 'data', 'aprovado']
    actions = [aprova_comentarios, reprova_comentarios]


admin.site.register(Comentario, ComentarioAdmin)
