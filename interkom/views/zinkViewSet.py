from django.http import Http404
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from interkom.serializers import *
from interkom.models import Galvanize
from rest_framework.validators import ValidationError


class ZinkViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Galvanize.objects.all()
    serializer_class = ZinkListSerializer
    permission_classes = [IsAdminUser, ]

    def get_serializer_class(self):
        serializer_class = ZinkListSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        queryset = Galvanize.objects.all()
        if not queryset:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            raise ValidationError("Запись создана, рабочие методы GET,PUT,DELETE")
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
