from django.urls import path

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
    path('marca_post/', views.marca_post, name="marca_post"),
]

