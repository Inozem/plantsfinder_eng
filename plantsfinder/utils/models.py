import uuid

from django.db import models


class ChoicesCharField(models.Model):
    CHOICES = ()
    name = models.CharField(
        max_length=50,
        verbose_name='Name',
        choices=CHOICES,
        unique=True,
        default=uuid.uuid1,
    )

    class Meta:
        ordering = ('id',)
        abstract = True

    def __str__(self):
        return self.name
