from django.db import models
from core.models import BaseModel


class OwnedByCompany(BaseModel):
    company = models.ForeignKey(
        "core.Company", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True