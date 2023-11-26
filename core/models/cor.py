from django.db import models


class Cor(models.Model):
    nome_cor = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_cor

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"
