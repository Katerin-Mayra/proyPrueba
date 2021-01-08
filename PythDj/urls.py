"""PythDj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from principal import views

#importar app con mis vistas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name="login"), #path('url_pagina', views.nombre_funcion, name="dar_nombre")
    path('check-user/', views.user_login, name="verificar"),            #verificar usuario
    path('login/', views.logout, name="log_out"),                        #deslogear
    path('inicio/<str:id>/', views.inicio_user, name="inicio"),                    #inicio de usuarios
    path('list-profiles/<str:id>/', views.list_profiles, name="perfiles"),
    
    path('create-user/<str:id>/', views.register_user, name="crear_user"),                 #formulario crear usuarios
    path('create-perfil/<str:id>/', views.register_profile, name="crear_perfil_admin"),    #formulario crear perfil
    
    path('delete-user/<str:id>/<str:id_user>/', views.delete_user, name="borrar_user"),                      #borrar usuario
    path('delete-profile/<str:id>/<str:id_profile>/', views.delete_profile, name="borrar_profile"),          #borrar perfil

    path('update-profile/<str:id>/', views.create_profile, name="crear_perfil"),                             #actualizar perfil usuario

    path('edit-user/<str:id>/<str:id_user>/', views.edit_user, name="editar_user"),                     #editar usuario
    path('edit-profile/<str:id>/<str:id_profile>/', views.edit_profile, name="editar_profile"),         #editar perfil
    
]

#usar la funcion url en las teplates
#usar el name en todas las path