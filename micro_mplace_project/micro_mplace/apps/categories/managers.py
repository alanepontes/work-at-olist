# Std libs imports

# Core django imports
from django.db import models

# Third party app imports

# Local apps


class ParentsCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=True)


class ChildsCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent__isnull=False)