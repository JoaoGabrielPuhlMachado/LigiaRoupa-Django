from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    CategoriaViewset,
    CompraViewset,
    CorViewset,
    MarcaViewset,
    ProdutoViewset,
    TamanhoViewset,
)
from uploader.router import router as uploader_router
from usuario.router import router as usuario_router

router = DefaultRouter()

router.register("categorias", CategoriaViewset, basename="categorias")
router.register("cores", CorViewset, basename="cores")
router.register("produtos", ProdutoViewset, basename="produtos")
router.register("compras", CompraViewset, basename="compras")
router.register("marcas", MarcaViewset, basename="marcas")
router.register("tamanhos", TamanhoViewset, basename="tamanhos")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
