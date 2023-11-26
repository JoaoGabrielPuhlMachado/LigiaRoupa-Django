from django.db import models

from uploader.models import Image


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    capa_categoria = models.ForeignKey(
        Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
