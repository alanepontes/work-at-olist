# Std libs imports
from itertools import zip_longest

# Core django imports
from django.core.management.base import BaseCommand, CommandError

# Third party app imports

# Local apps
from ....commons.utils import Util
from ...models import Category
from ....channels.models import Channel

class Command(BaseCommand):
    help = 'Import the channels and categories from csv file'

    def add_arguments(self, parser):
        parser.add_argument('channel', help='Channel name')
        parser.add_argument('categories_csv', help='File csv with categories to load')

    def handle(self, *args, **options):
        root, _ = next(Util.run_gen_csv_with_state(options['categories_csv']))
        
        channel, _ = Channel.objects.get_or_create(name=options['channel'])
        channel.category_set.all().delete()

        Category(name=root[0], channel=channel).save()
        for previous, current in Util.run_gen_csv_with_state(options['categories_csv']):
            previous_root, *previous_leafs = [category_root_to_leaf_path.strip() for category_root_to_leaf_path in previous[0].split('/')]
            current_root, *currents_leafs = [category_root_to_leaf_path.strip() for category_root_to_leaf_path in current[0].split('/')]
            if previous_root != current_root:
                Category(name=current_root, channel=channel).save()

            for item in zip_longest(previous_leafs, currents_leafs):
                p_leaf, c_leaf = item
                if p_leaf != c_leaf and c_leaf:
                   
                    if len(currents_leafs) == 1: 
                        parent, _ = Category.objects.get_or_create(name=current_root, parent__isnull=True)
                    else:
                        parent, _ = Category.objects.get_or_create(name=currents_leafs[-2], parent__isnull=False)

                    Category(name=c_leaf, channel=channel, parent=parent).save()
