from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from interkom.views import HomeViewSet

urlpatterns = [

    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type="text/xml")),
    path('api/', include('interkom.urls')),
    path('', HomeViewSet.index),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
