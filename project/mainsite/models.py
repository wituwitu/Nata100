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
    amigues = models.ManyToManyField("self", blank=True)  # many (user) to many (user)
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
    categoria = models.CharField(max_length=32, unique=True)
    tiempo = models.TimeField(blank=True, null=True)
    usuarie = models.ForeignKey(Alumne, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['tiempo']


class AbstractRanking(models.Model):
    marcas = models.ManyToManyField(Marca)  # many (marcas) to many (rankings)


class RankingRegional(AbstractRanking):
    tipo = 'regional'
    region = models.CharField(max_length=32, unique=True, primary_key=True)

    def __str__(self):
        return self.tipo


class RankingComunal(AbstractRanking):
    tipo = 'comunal'
    comuna = models.CharField(max_length=32, unique=True, primary_key=True)

    def __str__(self):
        return self.tipo


class RankingNacional(AbstractRanking):
    tipo = 'nacional'

    def __str__(self):
        return self.tipo


# - Crear los modelos para usuarios (listo), marcas, ranking, amigos y comentarios
# - Crear cronómetro (o ingreso de datos manual), que guarde el tiempo asociado al alumne, estilo de nado y otros datos importantes
# - Escoger si los datos se subirán a algún ranking o no
# - Recoger datos hacia los ránkings (tabla de mejores posiciones)
print('PyCharm')
