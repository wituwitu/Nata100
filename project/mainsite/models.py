from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"user_{instance.user.id}/{filename}"


class User(AbstractUser):
    # Attributes of User
    # Needed when creating an user
    username = models.CharField(max_length=32, unique=True, primary_key=True)
    email = models.EmailField()
    nacimiento = models.DateField(null=True)
    region = models.CharField(max_length=32, default="")
    comuna = models.CharField(max_length=32, default="")
    # Setting up some variables
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class Profe(User):

    def __str__(self):
        return self.username


class Alumne(User):
    profesor = models.ForeignKey(Profe, on_delete=models.CASCADE, null=True)  # one (profe) to many (alumne)

    def __str__(self):
        return self.username


class Marca(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    estilo = models.CharField(max_length=32, null=True)
    distancia = models.IntegerField(null=True)
    tiempo = models.TimeField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    comuna = models.CharField(max_length=32, null=True)
    region = models.CharField(max_length=32, null=True)
    publico = models.BooleanField(null=True)

    def to_str(self):
        return f"[{self.fecha}] {self.user.username}: {self.distancia} metros en {self.tiempo} ({self.estilo})"

    class Meta:
        ordering = ['tiempo']


class AbstractRanking(models.Model):
    marcas = models.ManyToManyField(Marca)  # many (marcas) to many (rankings)


class RankingComunal(AbstractRanking):
    comuna = models.CharField(max_length=32, unique=True, primary_key=True)


class RankingRegional(AbstractRanking):
    region = models.CharField(max_length=32, unique=True, primary_key=True)


class RankingNacional(AbstractRanking):
    pais = "chile"


class RankingAmigues(AbstractRanking):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Comentario(models.Model):
    profe = models.ForeignKey(Profe, on_delete=models.CASCADE, null=True)
    alumne = models.ForeignKey(Alumne, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(blank=True, null=True)
    texto = models.TextField(max_length=1024, blank=True, null=True)

    def to_str(self):
        return f"[{self.fecha}] Mensaje de {self.profe.username}: {self.texto}"

    def to_str_prof(self):
        return f"[{self.fecha}] Mensaje de {self.profe.username} a {self.alumne.username}: {self.texto}"
