"""
URL configuration for ticket_selling_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from ticket_selling_platform.settings import API_VERSION

BASE_PATH = f'api/{API_VERSION}'

schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1', ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f'{BASE_PATH}/user/', include('users.urls')),
    path(f'{BASE_PATH}/stadium/', include('stadiums.urls')),
    path(f'{BASE_PATH}/match/', include('matches.urls')),
    path(f'{BASE_PATH}/seat/', include('seats.urls')),
    path(f'{BASE_PATH}/ticketing/', include('ticketing.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
