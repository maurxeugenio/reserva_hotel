from django.db import models
from core.models import BaseModel


class Company(BaseModel):
    name = models.CharField(
        max_length=200,
        default=''
    )
    razao_social = models.CharField(
        max_length=200, 
        default=''
    )
    cnpj = models.CharField(
        max_length=200, 
        default=''
    )


    def __str__(self):
        return self.name