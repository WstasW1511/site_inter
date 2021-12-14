from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from interkom.serializers import *
from interkom.models import Home, Galvanize, Cuprum, ZinkSetModel


class HomeViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeListSerializer
    permission_classes = [IsAdminUser, ]

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




    def index(request):
        home = Home.objects.all()
        galvan = Galvanize.objects.all()
        cuprum = Cuprum.objects.all()
        zink_set = ZinkSetModel.objects.all()
        return render(request, 'interkom/index.html', {'home': home,
                                                       'galvan': galvan,
                                                       'cuprum': cuprum,
                                                       'zink_set': zink_set})
