"""demo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import REST.views
import REST.urls
from rest_framework import urls
from django.conf import settings # 미디어 파일 관련 설정 import
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('REST.urls')),
    path('api-auth/', include('rest_framework.urls'))   # 로그인 / 로그아웃 가능
]

# 미디어 파일 url, 폴더 위치 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
