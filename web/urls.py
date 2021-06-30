from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('nueva-publicacion', views.crear_publicacion, name='nueva_publicacion'),
    path('listar-publicaciones', views.listar_publicaciones, name='listar_publicaciones'),
    path('modificar-publicacion/<id>/',views.modificar_publicacion,name='modificar_publicacion'),
    path('eliminar-publicacion/<id>/', views.eliminar_publicacion, name='eliminar_publicacion')
]