from django.contrib import admin
from .models import Cargo, Funcionario, Servico


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo',)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','ativo','criado')


@admin.register(Servico)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo', 'criado')