from random import randint

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.models.fields import CharField, DecimalField, SlugField
from django.db.models.fields.related import ManyToManyField
from django.shortcuts import get_object_or_404

from plants.models import Deciduous

PLANT_CLASSES = [Deciduous, ]
TEST_DATA_AMOUNT = 35


class Command(BaseCommand):
    """Creates a test super-user and test data for the database."""
    help = 'Creates a test super-user and test data for the database.'

    def handle(self, *args, **options):
        User.objects.create_superuser('Anon', 'anon@test.com', 'qweqwe')

        for plant_class in PLANT_CLASSES:
            fields_comparison = (
                plant_class._meta.fields,
                plant_class._meta.many_to_many,
            )
            plant_fields = {}
            for fields in fields_comparison:
                for field in fields:
                    if '_ptr' not in field.name:
                        plant_fields[field.name] = field

            for _ in range(TEST_DATA_AMOUNT):
                self.create_plant(plant_class, plant_fields)

    def create_plant(self, plant_class, fields_and_names):
        """Creates plants."""
        data = {}
        many_to_many_fields = {}
        for field_name, field_model in fields_and_names.items():
            if ('ptr' not in field_name
                    and 'synonym' not in field_name
                    and field_name != 'id'):
                if (isinstance(field_model, CharField) or
                        isinstance(field_model, SlugField)):
                    choices = field_model.choices
                    if choices:
                        choice_number = randint(0, len(choices) - 1)
                        data[field_name] = choices[choice_number][0]
                    else:
                        data[field_name] = self.get_string_random()
                elif isinstance(field_model, DecimalField):
                    data[field_name] = self.get_number_random()
                elif isinstance(field_model, ManyToManyField):
                    many_to_many_fields[field_name] = field_model
        plant = plant_class.objects.create(**data)
        for field_name, field_model in many_to_many_fields.items():
            choices = [self.get_choice_random(field_model)
                       for _ in range(randint(1, 3))]
            getattr(plant, field_name).set(choices)

    def get_string_random(self):
        """Creates random string."""
        letters = [chr(randint(97, 122)) for _ in range(randint(5, 20))]
        return ''.join(letters).capitalize()

    def get_number_random(self):
        """Creates random number."""
        return randint(1, 14)

    def get_choice_random(self, model):
        """Makes a random selection."""
        field_model = model.related_model
        field_choices = field_model._meta.get_field('name').choices
        choice_number = randint(0, len(field_choices) - 1)
        choice = field_choices[choice_number][0]
        return get_object_or_404(field_model, name=choice)
