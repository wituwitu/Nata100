from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.frontPage, name="frontpage"),
    path('user/<str:userid>/', views.getUser, name="getuser"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.user_register, name="register"),
    path('formulario_alumne/', views.formulario_alumne, name="formulario_alumne"),
    path('formulario_alumne_post/', views.formulario_alumne_post, name="formulario_alumne_post"),
    path('formulario_profe/', views.formulario_profe, name="formulario_profe"),
    path('formulario_profe_post/', views.formulario_profe_post, name="formulario_profe_post"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('marca/', views.marca, name="marca"),
    path('marca_post/', views.marca_post, name="marca_post"),
    path('ranking_select/', views.ranking_select, name="ranking_select"),
    path('ranking_comunal/', views.ranking_comunal_index, name="ranking_comunal"),
    path('ranking_regional/', views.ranking_regional_index, name="ranking_regional"),
    path('ranking_nacional/', views.ranking_nacional_index, name="ranking_nacional"),
    path('agregar_amigue/', views.agregar_amigue, name="agregar_amigue"),
    path('aceptar_amigue/', views.aceptar_amigue, name="aceptar_amigue"),
    url(r'^friendship/', include('friendship.urls'))
]
