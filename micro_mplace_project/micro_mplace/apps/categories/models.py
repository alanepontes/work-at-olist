# Std libs imports

# Core django imports
from django.db import models

# Third party app imports

# Local apps
from .managers import ParentsCategoryManager
from .managers import ChildsCategoryManager
from ..commons.models import AbstractMetaModel
from ..channels.models import Channel


class Category(AbstractMetaModel):
    name = models.CharField(max_length=60, unique=True)
    channel = models.ForeignKey(Channel)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
   
    objects = models.Manager()
    only_parents_categories = ParentsCategoryManager()
    only_childs_categories = ChildsCategoryManager()

    def add_subcategories(self, name_subcategory):
        subcategory, created = Category.objects.get_or_create(name=name_subcategory, channel=self.channel)
        if created:
            subcategory.parent = self.parent 

    def subcategories(self, only_child=False):
        if only_child:
            return Category.objects.filter(parent=self)
        return [subcategory for subcategory in self.gen_subcategories()]

    def parent_categories(self, only_parent=False):
        if only_parent:
            return self.parent
        return [category for category in self.gen_category()]

    def gen_subcategories(self):
        for subcategory in Category.objects.filter(parent=self):
            yield from subcategory.gen_subcategories()
            yield subcategory

    def gen_category(self):
        if self.parent:
            yield self.parent
            yield from self.parent.gen_category()

    def __str__(self):
        return self.name

