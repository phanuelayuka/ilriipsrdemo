"""ipsrdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ipsrdemo.settings import base as settings


urlpatterns = [
    path('', include('profiles.urls')),
    path('core/', include('core.urls')),
    # path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
