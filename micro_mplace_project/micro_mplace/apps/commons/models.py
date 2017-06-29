# Std libs imports
import uuid

# Core django imports
from django.db import models

# Third party app imports

# Local apps


class AbstractMetaModel(models.Model):
   	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 

    class Meta:
        abstract = True

    
