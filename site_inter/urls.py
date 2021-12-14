
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from interkom.views import HomeViewSet

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('interkom.urls')),
    path('', HomeViewSet.index)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
