from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import (
    ProdutoDetailSerializer,
    ProdutoListSerializer,
    ProdutoSerializer,
)


class ProdutoViewset(ModelViewSet):
    queryset = Produto.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["categoria__descricao", "marca__nome_marca", "cor__nome_cor", "tamanho__especificacao"]
    search_fields = ["nome"]
    ordering_fields = ["nome", "preco"]
    ordering = ["nome"]

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer
