from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome=models.CharField(max_length=100, null=False, blank=False)
    idade=models.IntegerField(null=False,blank=False)
    data_nascimento=models.DateTimeField(null=False,blank=False)
    is_ativo=models.BooleanField(null=False,default=True)
