"""
Django admin customization.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Categoria, Compra, Cor, ItensCompra, Marca, Produto, Tamanho


class ItensCompraInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("nome_marca",)
    search_fields = ("nome_marca",)
    list_filter = ("nome_marca",)
    ordering = ("nome_marca",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ("nome_cor",)
    search_fields = ("nome_cor",)
    list_filter = ("nome_cor",)
    ordering = ("nome_cor",)


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ("especificacao",)
    search_fields = ("especificacao",)
    list_filter = ("especificacao",)
    ordering = ("especificacao",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "categoria",
        "cor",
        "marca",
        "tamanho",
    )
    search_fields = (
        "nome",
        "categoria__descricao",
        "nome_cor",
        "nome_marca",
        "especificacao",
    )
    list_filter = (
        "categoria",
        "cor",
        "marca",
        "tamanho",
    )
    ordering = (
        "nome",
        "categoria",
        "cor",
        "marca",
    )
    list_per_page = 25
