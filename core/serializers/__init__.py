from .categoria import CategoriaSerializer
from .cor import CorSerializer
from .produto import ProdutoSerializer, ProdutoDetailSerializer, ProdutoListSerializer
from .marca import MarcaSerializer
from .tamanho import TamanhoSerializer
from .compras import (
    CompraSerializer,
    ItensCompraSerializer,
    CriarEditarCompraSerializer,
    CriarEditarItensCompraSerializer,
)
from .mytoken import MyTokenObtainPairSerializer
