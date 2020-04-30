from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator


class Car(models.Model):
    """Database model for Car in the system"""
    SEDAN = 'SE'
    SUV = 'SU'
    COUPE = 'CO'
    HATCHBACK = 'HA'
    PICKUP = 'PI'
    STATION_WAGON = 'SW'
    OTHER = 'OT'
    CATEGORY_CHOICES = [
        (SEDAN, 'Sedán'),
        (SUV, 'SUV'),
        (COUPE, 'Coupé'),
        (HATCHBACK, 'Hatchback'),
        (PICKUP, 'Pick-up'),
        (STATION_WAGON, 'Station Wagon'),
        (OTHER, 'Otro')
    ]
    code = models.CharField(max_length=255, blank=True, default='C000001')
    category = models.CharField(max_length=2,
                                choices=CATEGORY_CHOICES,
                                blank=False)
    model = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    number_of_doors = models.PositiveSmallIntegerField(
        blank=False,
        validators=[
            MaxValueValidator(5)
        ])
    is_diesel = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255,
                                   blank=True,
                                   default='Description not provided')
    current_owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.PROTECT,
                                      null=True)

    def get_full_name(self):
        """Retrieve full name of the car"""
        return self.category+self.model+self.name

    def get_short_name(self):
        """Retrieve short name of the car"""
        return self.name

    def __str__(self):
        """Retrieve String representation of the car"""
        return f'Categoría: {self.category}, Modelo: {self.model},\
                Nombre: {self.name}'
