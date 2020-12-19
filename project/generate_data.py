import os
import sys

import django

sys.path.append("/project")
print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from sqlite3.dbapi2 import Date, Time

from friendship.models import Friend, FriendshipRequest

from mainsite.models import Profe, Alumne, Marca
from mainsite.views import ranking_comunal, ranking_regional, ranking_nacional


print("Creando profes")
jorge_sandoval = Profe.objects.create_user(username="Jorge Sandoval",
                                           email="jorge@sandoval.cl",
                                           password="soyAdmin")
dasla_pando = Profe.objects.create_user(username="Dasla Pando",
                                        email="dasla@pando.cl",
                                        password="soyAdmin")

print("Personalizando profes")

jorge_sandoval.nacimiento = Date(1977, 11, 4)
jorge_sandoval.comuna = "Santiago"
jorge_sandoval.region = "Región Metropolitana de Santiago"
jorge_sandoval.save()
dasla_pando.nacimiento = Date(1995, 9, 16)
dasla_pando.comuna = "Santiago"
dasla_pando.comuna = "Región Metropolitana de Santiago"
dasla_pando.save()

print("Creando alumnes")
catalina_gamboa = Alumne.objects.create_user(username="Catalina Gamboa",
                                             email="catalina@gamboa.cl",
                                             password="soyAdmin")
barbara_rocco = Alumne.objects.create_user(username="Bárbara Rocco",
                                           email="barbara@rocco.cl",
                                           password="soyAdmin")
claudia_san_martin = Alumne.objects.create_user(username="Claudia San Martín",
                                                email="claudia@sanmartin.cl",
                                                password="soyAdmin")
diego_wistuba = Alumne.objects.create_user(username="Diego Wistuba",
                                           email="diego@wistuba.cl",
                                           password="soyAdmin")

print("Personalizando alumnes")

catalina_gamboa.nacimiento = Date(1996, 12, 8)
catalina_gamboa.comuna = "Maipú"
catalina_gamboa.region = "Región Metropolitana de Santiago"
catalina_gamboa.profesor = jorge_sandoval
catalina_gamboa.save()
barbara_rocco.nacimiento = Date(1996, 3, 5)
barbara_rocco.comuna = "Peñalolén"
barbara_rocco.region = "Región Metropolitana de Santiago"
barbara_rocco.profesor = jorge_sandoval
barbara_rocco.save()
claudia_san_martin.nacimiento = Date(1996, 5, 28)
claudia_san_martin.comuna = "San Miguel"
claudia_san_martin.region = "Región Metropolitana de Santiago"
claudia_san_martin.profesor = dasla_pando
claudia_san_martin.save()
diego_wistuba.nacimiento = Date(1997, 6, 15)
diego_wistuba.comuna = "Quilicura"
diego_wistuba.region = "Región Metropolitana de Santiago"
diego_wistuba.profesor = dasla_pando
diego_wistuba.save()

print("Haciendo amistades")
Friend.objects.add_friend(from_user=catalina_gamboa,
                          to_user=barbara_rocco)
FriendshipRequest.objects.get(to_user=barbara_rocco,
                              from_user=catalina_gamboa).accept()
Friend.objects.add_friend(from_user=catalina_gamboa,
                          to_user=claudia_san_martin)
FriendshipRequest.objects.get(to_user=claudia_san_martin,
                              from_user=catalina_gamboa).accept()
Friend.objects.add_friend(from_user=catalina_gamboa,
                          to_user=diego_wistuba)
FriendshipRequest.objects.get(to_user=diego_wistuba,
                              from_user=catalina_gamboa).accept()
Friend.objects.add_friend(from_user=barbara_rocco,
                          to_user=claudia_san_martin)
FriendshipRequest.objects.get(to_user=claudia_san_martin,
                              from_user=barbara_rocco).accept()
Friend.objects.add_friend(from_user=barbara_rocco,
                          to_user=diego_wistuba)
FriendshipRequest.objects.get(to_user=diego_wistuba,
                              from_user=barbara_rocco).accept()
Friend.objects.add_friend(from_user=claudia_san_martin,
                          to_user=diego_wistuba)
FriendshipRequest.objects.get(to_user=diego_wistuba,
                              from_user=claudia_san_martin).accept()

print("Agregando marcas")
marca = Marca.objects.create(user=catalina_gamboa,
                             estilo="Crol",
                             distancia=25,
                             tiempo=Time(minute=3, second=10),
                             comuna=catalina_gamboa.comuna,
                             region=catalina_gamboa.region,
                             publico=True)
marca.publico = False
marca = Marca.objects.create(user=catalina_gamboa,
                             estilo="Mariposa",
                             distancia=25,
                             tiempo=Time(minute=2, second=50),
                             comuna=catalina_gamboa.comuna,
                             region=catalina_gamboa.region,
                             publico=True)
ranking_nacional(marca)
ranking_regional(marca)
ranking_comunal(marca)
_ = Marca.objects.create(user=barbara_rocco,
                         estilo="Espalda",
                         distancia=50,
                         tiempo=Time(minute=4, second=30),
                         comuna=barbara_rocco.comuna,
                         region=barbara_rocco.region,
                         publico=True)
_ = Marca.objects.create(user=barbara_rocco,
                         estilo="Crol",
                         distancia=50,
                         tiempo=Time(minute=4, second=10),
                         comuna=barbara_rocco.comuna,
                         region=barbara_rocco.region,
                         publico=True)
_ = Marca.objects.create(user=claudia_san_martin,
                         estilo="Pecho",
                         distancia=25,
                         tiempo=Time(minute=3, second=10),
                         comuna=claudia_san_martin.comuna,
                         region=claudia_san_martin.region,
                         publico=True)
marca = Marca.objects.create(user=claudia_san_martin,
                             estilo="Crol",
                             distancia=50,
                             tiempo=Time(minute=4, second=20),
                             comuna=claudia_san_martin.comuna,
                             region=claudia_san_martin.region,
                             publico=True)
ranking_nacional(marca)
ranking_regional(marca)
ranking_comunal(marca)
marca = Marca.objects.create(user=diego_wistuba,
                             estilo="Mariposa",
                             distancia=50,
                             tiempo=Time(minute=3, second=30),
                             comuna=diego_wistuba.comuna,
                             region=diego_wistuba.region,
                             publico=True)
ranking_nacional(marca)
ranking_regional(marca)
ranking_comunal(marca)
marca = Marca.objects.create(user=diego_wistuba,
                             estilo="Espalda",
                             distancia=100,
                             tiempo=Time(minute=5, second=20),
                             comuna=diego_wistuba.comuna,
                             region=diego_wistuba.region,
                             publico=True)
ranking_nacional(marca)
ranking_regional(marca)
ranking_comunal(marca)
