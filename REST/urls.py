from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)
router.register('album', views.ImageViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
