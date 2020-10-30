from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontPage, name="frontpage"),
    path('user/<str:userid>/', views.getUser, name="getuser"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.user_register, name="register"),
    path('formulario/', views.formulario, name="formulario"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
