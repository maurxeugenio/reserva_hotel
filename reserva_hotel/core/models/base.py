from django.db import models
from functools import partial
from core.utils import generate_random_code


class BaseModel(models.Model):
    code = models.CharField(
        max_length=50,
        default=partial(generate_random_code),
        unique=False,
        db_index=True
    )
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    deleted_by = models.ForeignKey(
        'core.User',
        related_name='%(class)s_deleted_by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True