from django.db import models

from core.models import Categoria, Cor, Marca, Tamanho
from uploader.models import Image


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="itens")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="itens")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="itens")
    tamanho = models.ForeignKey(Tamanho, on_delete=models.PROTECT, related_name="itens")
    capa = models.ForeignKey(Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f"Nome: {self.nome}. Categoria: {self.categoria}. Marca: {self.marca}. Cor: {self.cor}. Tamanho: {self.tamanho}  Estoque: ({self.quantidade})."

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
