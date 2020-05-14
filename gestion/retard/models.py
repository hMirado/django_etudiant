from django.db import models
from etudiant.models import Etudiant
# Create your models here.

class Retard(models.Model):
    identifiant = models.CharField(max_length = 10)
    semestre = models.CharField(max_length = 3, null = True)
    niveau	=	models.CharField(max_length = 10)
    matiere = models.CharField(max_length = 250)
    date = models.DateTimeField(auto_now_add=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True)
