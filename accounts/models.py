from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): 
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
    cpf = models.CharField("CPF", max_length=11, null=True, blank=True)

class CustomUser(AbstractUser):
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
    cpf = models.CharField("CPF", max_length=11, null=True, blank=True)
    imagem = models.FileField(
        upload_to='images',
        default=None,
        null=True
)
