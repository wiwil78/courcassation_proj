"""
URL configuration for courcassation_proj project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    # =========================
    # ADMINISTRATION
    # =========================
    path('admin/', admin.site.urls),

    # =========================
    # APPLICATION PRINCIPALE
    # =========================
    path('', include('arret.urls')),
]


# =========================
# FICHIERS MEDIA / PDF
# =========================
# Permet de servir les fichiers PDF stockés dans MEDIA_ROOT,
# même lorsque DEBUG = False.
urlpatterns += [
    path(
        'media/<path:path>',
        serve,
        {
            'document_root': settings.MEDIA_ROOT,
        },
    ),
]