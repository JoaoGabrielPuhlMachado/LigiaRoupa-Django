from django.db import models

from uploader.models import Image


class Marca(models.Model):
    nome_marca = models.CharField(max_length=50)
    logo_marca = models.ForeignKey(
        Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.nome_marca

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
