from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class UserViewSet(viewsets.ModelViewSet):
    pass  # TODO: add get (all), get, edit, create, delete methods
