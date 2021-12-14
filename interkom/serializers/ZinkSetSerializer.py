from rest_framework import serializers
from interkom.models import ZinkSetModel


class ZinkSetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZinkSetModel
        fields = (
            'uuid',
            'title',
            'zinks_image_1',
            'description_image1',
            'zinks_image_2',
            'description_image2',
            'zinks_image_3',
            'description_image3'
        )
