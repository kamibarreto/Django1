from django.contrib import admin

# Register your models here.

from devpro.encurtador.models import UrlRedirect, UrlLog

@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destino', 'slug', 'criado_em','atualizado_em')

@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):
    list_display = ('origem', 'criado_em', 'user_agent', 'host', 'ip', 'url_redirect')
    def has_change_permission(self, request, obj=None):
        return False
    #este acima, serve para dar permissão de alteração, sobre o url log por exemplo
    def has_delete_permission(self, request, obj=None):
        return False
    #mesma coisa do de cima, permissão para deletar o urllog, coloquei False para não dar acesso a isso
    def has_add_permission(self, request):
        return False
    #remover o adicionar mais url
