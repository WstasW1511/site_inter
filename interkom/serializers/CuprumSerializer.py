from rest_framework import serializers
from interkom.models import Cuprum


class CuprumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuprum
        fields = (
            'uuid',
            'title',
            'description_cuprum',
            'cuprum_set',
            'cuprum_image_1',
            'description_image1',
            'cuprum_image_2',
            'description_image2',
            'cuprum_image_3',
            'description_image3'
        )
