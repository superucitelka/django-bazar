"""bazarweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from bazarweb import settings

"""
    URL mapování - nastavení základních URL adres aplikace
"""
urlpatterns = [
    # Nastavení URL adresy pro přístup k administraci
    path('admin/', admin.site.urls),
    # Přesměrování na lokální URL mapper aplikace bazar
    path('bazar/', include('bazar.urls')),
    # Přesměrování domovské stránky na úvodní stránku aplikace bazar
    path('', RedirectView.as_view(url='bazar/')),
]

# Připojení cest k statickým souborům, které definují konstanty v settings.py
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
