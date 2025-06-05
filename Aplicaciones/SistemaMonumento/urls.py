from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name='inicio'),  
    path('listar_monumento/', views.listar_monumento, name='listar_monumento'),
    path('nuevo_monumento/', views.nuevo_monumento, name='nuevo_monumento'), 
    path('guardar_monumento/', views.guardar_monumento, name='guardar_monumento'),
    path('eliminar_monumento/<int:id>/', views.eliminar_monumento, name='eliminar_monumento'),
    path('editar_monumento/<int:id>/', views.editar_monumento, name='editar_monumento'),
    path('procesar_edicion_monumento/', views.procesar_edicion_monumento, name='procesar_edicion_monumento'),



]