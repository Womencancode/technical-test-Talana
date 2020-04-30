from rest_framework import serializers

from car.models import Car


class CarListSerializer(serializers.ModelSerializer):
    """Serializes a car object for list them all"""

    class Meta:
        model = Car
        fields = (
            'id',
            'category',
            'model',
            'name',
            'number_of_doors'
        )


class CarSerializer(serializers.ModelSerializer):
    """Serializes a car object post, put and patch"""

    class Meta:
        model = Car
        fields = (
            'id',
            'category',
            'model',
            'name',
            'number_of_doors'
        )

    def create(self, validated_data):
        """Create and  return  new user"""
        car = Car.objects.create(**validated_data)
        return car


class CarDetailSerializer(serializers.ModelSerializer):
    """Serializes a car object for detail"""
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Car
        fields = '__all__'
