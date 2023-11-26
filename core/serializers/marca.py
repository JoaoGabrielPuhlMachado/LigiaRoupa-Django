from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Marca
from uploader.models import Image
from uploader.serializers import ImageSerializer


class MarcaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="logo_marca",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    logo_marca = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Marca
        fields = "__all__"
        depth = 1
