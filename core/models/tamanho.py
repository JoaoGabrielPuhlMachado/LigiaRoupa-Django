from django.db import models


class Tamanho(models.Model):
    especificacao = models.CharField(max_length=10)

    def __str__(self):
        return self.especificacao

    class Meta:
        verbose_name = "Tamanho"
        verbose_name_plural = "Tamanhos"
