# Std libs imports

# Core django imports
from django.db import models

# Third party app imports

# Local apps
from ..commons.models import AbstractMetaModel

class Channel(AbstractMetaModel):
    name = models.CharField(max_length=60, unique=True)
   
    def __str__(self):
        return self.name

