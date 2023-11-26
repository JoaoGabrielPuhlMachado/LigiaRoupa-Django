from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Categoria
from uploader.models import Image
from uploader.serializers import ImageSerializer


class CategoriaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa_categoria",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa_categoria = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Categoria
        fields = "__all__"
        depth = 1
