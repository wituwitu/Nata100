from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context
from django.views import generic

from .models import User, Alumne, Profe, RankingNacional, RankingRegional, RankingComunal, Marca, RankingAmigues

from .models import User, Alumne, Profe

from friendship.models import Friend, Follow, Block, FriendshipRequest


def frontPage(request):
    """
    The view for the front page
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            return dashboard(request)
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
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return dashboard(request)
        else:
            return HttpResponseRedirect('/')


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
            user.profesor = Profe.objects.get(pk=profe)
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
    persona = Alumne.objects.filter(username=user.username)
    if persona.exists():
        persona = persona[0]
        c = {'username': persona.username,
             'email': persona.email,
             'nacimiento': persona.nacimiento,
             'profe': persona.profesor,
             'region': persona.region,
             'comuna': persona.comuna,
             'solicitudes': Friend.objects.unrejected_requests(user=request.user)}
        return render(request, "frontPage/dashboard_alumne.html", context=c)
    else:
        persona = Profe.objects.filter(username=user.username)
        if persona.exists():
            persona = persona[0]
            c = {'username': persona.username,
                 'email': persona.email,
                 'nacimiento': persona.nacimiento,
                 'region': persona.region,
                 'comuna': persona.comuna,
                 'alumnes': list(Alumne.objects.filter(profesor=request.user))}
            return render(request, "frontPage/dashboard_profe.html", context=c)
        else:
            raise Http404("Le usuarie no existe.")


def marca(request):
    return render(request, "frontPage/marca.html")


def marca_profe(request):
    alumnes = list(Alumne.objects.filter(profesor=request.user))
    c = {'alumnes': alumnes}
    return render(request, "frontPage/marca_profe.html", context=c)


def mis_marcas(request):
    marcas = list(Marca.objects.filter(user=request.user).order_by("fecha"))
    c = {"marcas": marcas}
    return render(request, "frontPage/mis_marcas.html", context=c)


def marca_post(request):
    if request.method == 'POST':
        if "alumne" in request.POST.keys():
            user = Alumne.objects.get(username=request.POST["alumne"])
        else:
            user = request.user
        tipo = request.POST["tipo"]
        estilo = request.POST["estilo"]
        distancia = request.POST["distancia"]
        tiempo = request.POST["tiempo"]
        comuna = request.POST["comunas"]
        region = request.POST["regiones"]

        m = Marca.objects.create(user=user,
                                 estilo=estilo,
                                 distancia=distancia,
                                 tiempo=tiempo,
                                 comuna=comuna,
                                 region=region,
                                 publico=True)

        if tipo == "comunal":
            ranking_comunal(m)
        elif tipo == "regional":
            ranking_comunal(m)
        elif tipo == "nacional":
            ranking_nacional(m)
        elif tipo == "amigues":
            pass
        elif tipo == "ninguno":
            m.publico = False
            m.save()

    return dashboard(request)


def ranking_comunal(m):
    comuna = m.comuna
    rankings = RankingComunal.objects.filter(comuna=comuna)
    if not rankings.exists():
        ranking = RankingComunal.objects.create(comuna=comuna)
    else:
        ranking = rankings[0]
    ranking.marcas.add(m)
    ranking.save()


def ranking_regional(m):
    region = m.region
    rankings = RankingRegional.objects.filter(region=region)
    if not rankings.exists():
        ranking = RankingRegional.objects.create(region=region)
    else:
        ranking = rankings[0]
    ranking.marcas.add(m)
    ranking.save()


def ranking_nacional(m):
    rankings = RankingNacional.objects.all()
    if not rankings.exists():
        ranking = RankingNacional.objects.create()
    else:
        ranking = rankings[0]
    ranking.marcas.add(m)
    ranking.save()


def ranking_select(request):
    if request.method == "POST":
        tipo = request.POST["tipo"]
        if tipo == "comunal":
            return ranking_comunal_index(request, request.POST["comunas"])
        elif tipo == "regional":
            return ranking_regional_index(request, request.POST["regiones"])
        elif tipo == "nacional":
            return ranking_nacional_index(request)
        elif tipo == "amigues":
            return ranking_amigues_index(request)


def ranking_comunal_index(request, comuna):
    ranking = get_object_or_404(RankingComunal, comuna=comuna)
    top_10 = ranking.marcas.all().order_by("tiempo")[:10]
    context = {"comuna": comuna, "top_10": top_10}

    return render(request, "frontPage/ranking_comunal.html", context)


def ranking_regional_index(request, region):
    ranking = get_object_or_404(RankingRegional, region=region)
    top_10 = ranking.marcas.all().order_by("tiempo")[:10]
    context = {"region": region, "top_10": top_10}

    return render(request, "frontPage/ranking_regional.html", context)


def ranking_nacional_index(request):
    ranking = get_object_or_404(RankingNacional)
    top_10 = ranking.marcas.all().order_by("tiempo")[:10]
    context = {"pais": "Chile", "top_10": top_10}

    return render(request, "frontPage/ranking_nacional.html", context)


def ranking_amigues_index(request):
    amigues = Friend.objects.friends(request.user)
    top_10 = Marca.objects.filter(user__in=amigues).exclude(publico=False).order_by("tiempo")[:10]
    context = {"top_10": top_10}
    return render(request, "frontPage/ranking_amigues.html", context)


def agregar_amigue(request):
    if request.method == "POST":
        amigue = User.objects.get(pk=request.POST["amigue"])
        Friend.objects.add_friend(from_user=request.user,
                                  to_user=amigue,
                                  message="Seamos amigues en Nata100!")
    return dashboard(request)


def aceptar_amigue(request):
    if request.method == "POST":
        solicitud = FriendshipRequest.objects.get(to_user=request.user,
                                                  from_user=User.objects.get(pk=request.POST["amigue"]))
        solicitud.accept()
    return dashboard(request)


def modo_recreativo(request):
    return render(request, "frontPage/modo_recreativo.html")
