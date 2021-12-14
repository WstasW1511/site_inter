from django.urls import path
from rest_framework.routers import DefaultRouter
from interkom.views import HomeViewSet, ZinkViewSet, CuprumViewSet, ZinkSetViewSet


router = DefaultRouter()

router.register('home', HomeViewSet)
router.register('galvan', ZinkViewSet)
router.register('cuprum', CuprumViewSet)
router.register('zinks', ZinkSetViewSet)

urlpatterns = [

]+router.urls
