from django.test import TestCase
from car import models


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new car is successful"""
        category = 'CO'
        model = "TT RS 2020"
        name = 'Audi TT RS TURBO'
        number_of_doors = 3
        description = 'This car is a beast'
        car = models.Car.objects.create(
            category=category,
            model=model,
            name=name,
            number_of_doors=number_of_doors,
            description=description
        )

        self.assertEqual(car.category, category)
        self.assertEqual(car.model, model)
        self.assertEqual(car.name, name)
        self.assertEqual(car.number_of_doors, number_of_doors)
        self.assertEqual(car.description, description)
