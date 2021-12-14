from rest_framework import serializers
from interkom.models import Galvanize


class ZinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galvanize
        fields = (
            'uuid',
            'title',
            'description_galvanize',
            'zink_image_1',
            'description_image1',
            'zink_image_2',
            'description_image2',
            'zink_image_3',
            'description_image3'
        )
