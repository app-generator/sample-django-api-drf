from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class TransactionViewSetCreate(viewsets.GenericViewSet, mixins.CreateModelMixin):
    pass


class TransactionViewSetDelete(viewsets.GenericViewSet, mixins.DestroyModelMixin):
    pass


class TransactionViewSetUpdate(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    pass


class TransactionViewSetList(viewsets.GenericViewSet, mixins.ListModelMixin):
    pass


class TransactionViewSetRetrieve(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    pass
