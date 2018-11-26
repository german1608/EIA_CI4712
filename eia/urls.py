"""eia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from eia_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'consultor-crud/',
        views.consultor_index,
        name='consultor-crud-index'),
    path(
        'consultor-crud/',
        include(
            'eia_app.urls',
            namespace='consultor-crud')),
    path(
        'medidas/',
        include(
            'medidas.urls',
            namespace='medidas')),
    path('users/', include("users.urls")),
    path('', include('dashboard.urls')),
    path('configuracion/', include("configuracion.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, },
            name='media'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

