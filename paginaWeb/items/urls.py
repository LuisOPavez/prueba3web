from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('nuevo/', views.item_create, name='item_create'),
    path('<str:pk>/editar/', views.item_edit, name='item_edit'),
    path('<str:pk>/eliminar/', views.item_delete, name='item_delete'),
    path('<str:pk>/', views.item_detail, name='item_detail'),
]
