from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from interkom.serializers import *
from interkom.models import Cuprum


class CuprumViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Cuprum.objects.all()
    serializer_class = CuprumListSerializer
    permission_classes = [IsAdminUser, ]

    def get_serializer_class(self):
        serializer_class = CuprumListSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
