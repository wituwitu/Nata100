from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from .models import User


def frontPage(request):
    """
    The view for the front page
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, "frontPage/dashboard.html")
        else:
            return render(request, 'frontPage/index_kurisu.html')


def getUser(request, userid):
    """
    The view to request an user profile
    """
    if request.method == 'GET':
        # TODO implement
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
    if request.method == 'GET':
        return render(request, 'user/register.html')

    elif request.method == 'POST':
        attributes = {"username": None, "email": None, "discord-tag": None, "password": None}
        optional = ["tagSteam", "tagPSN", "tagXbox", "tagSwitch"]

        for element in attributes.keys():
            if element not in request.POST:
                return HttpResponseRedirect("/register/")

        for element in optional:
            if element in request.POST:
                attributes[element] = request.POST[element]

        _ = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], tagDiscord=request.POST["discord-tag"], password=request.POST["password"])

        return HttpResponseRedirect('/formulario/')


def formulario(request):
    return render(request, 'frontPage/formulario.html')


def dashboard(request):
    return render(request, "frontPage/dashboard.html")
