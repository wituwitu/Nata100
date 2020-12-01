from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import Context
from .models import User, Alumne, Profe, RankingNacional, RankingRegional, RankingComunal

from .models import User, Alumne, Profe


def frontPage(request):
    """
    The view for the front page
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, "frontPage/dashboard.html")
        else:
            return render(request, 'frontPage/index.html')


def getUser(request, userid):
    """
    The view to request an user profile
    """
    if request.method == 'GET':
        return render(request, "user/profile.html")


def user_login(request):
    """
    The login view
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, 'user/login.html')

    elif request.method == "POST":
        if "username" in request.POST.keys():
            username = request.POST["username"]
            password = request.POST['password']
        else:
            pass

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/login/')


def user_logout(request):
    """
    A simple view to logout the session
    """
    logout(request)
    return HttpResponseRedirect('/')


def user_register(request):
    """
    The register view
    """
    if request.method == 'POST':

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if request.POST["tipo_usuario"] == "0":
            _ = Alumne.objects.create_user(username=username, email=email,
                                           password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return formulario_alumne(request)

        elif request.POST["tipo_usuario"] == "1":
            _ = Profe.objects.create_user(username=username, email=email,
                                          password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return formulario_profe(request)


def formulario_alumne(request):
    profe_list = Profe.objects.all()
    username = request.user.username
    c = {'username': username, 'profe_list': profe_list}
    return render(request, 'frontPage/formulario_alumne.html', context=c)


def formulario_profe(request):
    return render(request, 'frontPage/formulario_profe.html')


def formulario_alumne_post(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            nacimiento = request.POST["nacimiento"]
            region = request.POST["regiones"]
            comuna = request.POST["comunas"]
            profe = request.POST["profe"]
            user.nacimiento = nacimiento
            user.region = region
            user.comuna = comuna
            user.profesor = profe
            user.save()
    return dashboard(request)


def formulario_profe_post(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            nacimiento = request.POST["nacimiento"]
            region = request.POST["regiones"]
            comuna = request.POST["comunas"]
            user.nacimiento = nacimiento
            user.region = region
            user.comuna = comuna
            user.save()
    return dashboard(request)


def dashboard(request):
    user = request.user
    c = {'username': user.username, 'email': user.email, 'nacimiento': user.nacimiento, 'profe': user.profesor,
         'region': user.region, 'comuna': user.comuna, 'amigues': user.amigues}
    return render(request, "frontPage/dashboard.html", context=c)

def Ranking_Comunal(request):
    tipo=RankingComunal.objects.all()
    if request.method=='POST':
        tiempo = request.POST["tiempo"]
        usuario = request.user
        tipo.tiempo=tiempo
        tipo.usuario=usuario
        tipo.save()
    return dashboard(request)

def Ranking_Regional(request):
    tipo=RankingRegional.objects.all()
    if request.method=='POST':
        tiempo = request.POST["tiempo"]
        usuario = request.user
        tipo.tiempo=tiempo
        tipo.usuario=usuario
        tipo.save()
    return dashboard(request)

def Ranking_Nacional(request):
    tipo=RankingNacional.objects.all()
    if request.method=='POST':
        tiempo = request.POST["tiempo"]
        usuario = request.user
        tipo.tiempo=tiempo
        tipo.usuario=usuario
        tipo.save()
    return dashboard(request)