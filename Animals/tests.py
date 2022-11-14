from django.test import TestCase
from Animals.models import Animal


class AnimalsTestCase(TestCase):
    def test_animals_registered(self):
        all_animals = Animal.objects.all()

        print(all_animals)
        self.assertEqual(len(all_animals), 2)
