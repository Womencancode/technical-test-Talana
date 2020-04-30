from django.http import Http404
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user import serializers


class UserList(APIView):
    """List all users, or create a new user."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        users = get_user_model().objects.all()
        serializer = serializers.UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """Retrieve, update, patch or delete a user instance."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        try:
            return self.request.user
        except get_user_model().DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user = self.get_object()
        serializer = serializers.UserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, format=None):
        user = self.get_object()
        serializer = serializers.UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        user = self.get_object()
        serializer = serializers.UserUpdateSerializer(user, data=request.data,
                                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateTokeView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializers_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
