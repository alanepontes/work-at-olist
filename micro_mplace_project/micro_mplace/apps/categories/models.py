# Std libs imports

# Core django imports
from django.db import models

# Third party app imports

# Local apps
from ..commons.models import AbstractMetaModel
from ..channels.models import Channel


class Category(AbstractMetaModel):
    name = models.CharField(max_length=60, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel)
   
    def __str__(self):
        return self.name

