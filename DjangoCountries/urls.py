"""DjangoCountries URL Configuration

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
from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="home-page"),
    #  path('item/<int:id>/', views.item),
    path('country/<country_name>/', views.func_country, name="country-page"),
    path('countries-list/', views.func_countries, name="country-list-page"),
    path('languages/', views.func_languages, name="languages-page"),
    path('countries_by_language/<language_name>/', views.func_countries_by_language, name="countries_by_language-page"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
