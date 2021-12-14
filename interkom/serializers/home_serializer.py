from rest_framework.serializers import ModelSerializer
from interkom.models import Home


class HomeListSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = (
            'uuid',
            'title',
            'welcome',
        )
