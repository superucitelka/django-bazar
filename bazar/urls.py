from django.urls import path
from . import views

# URL mapování - seznam URL adres pro aplikaci bazar
urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.BazarListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.BazarDetailView.as_view(), name='detail'),
    path('zbozi/create/', views.ZboziCreate.as_view(), name='zbozi-create'),
    path('zbozi/<int:pk>/update/', views.ZboziUpdate.as_view(), name='zbozi-update'),
    path('zbozi/<int:pk>/delete/', views.ZboziDelete.as_view(), name='zbozi-delete'),
]