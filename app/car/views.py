from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from car import models
from car import serializers


class CarList(APIView):
    """List all cars, or create a new car."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        cars = models.Car.objects.all()
        serializer = serializers.CarListSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetail(APIView):
    """Retrieve, update, patch or delete a car instance."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return models.Car.objects.get(pk=pk)
        except models.Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = serializers.CarDetailSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = serializers.CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = serializers.CarSerializer(car, data=request.data,
                                               partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
