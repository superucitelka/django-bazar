from django.urls import path
from . import views

# URL mapování - seznam URL adres pro aplikaci bazar
urlpatterns = [
    path('', views.index, name='index'),
]