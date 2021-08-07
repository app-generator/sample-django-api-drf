from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound, MethodNotAllowed
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist

from api.transaction.models import Transaction
from api.transaction.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    not_found_message = {"success": False, "msg": "This object doesn't exist."}
    missing_id_message = {"success": False, "msg": "Provide a transaction id."}

    def get_queryset(self):
        return Transaction.objects.all()

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')

    @action(methods=['get'], detail=False, url_path='get')
    def get_transactions(self, request, *args, **kwargs):

        transactions = self.get_queryset()

        page = self.paginate_queryset(transactions)

        if page is not None:
            serializer = self.get_serializer(page, many=True, context=self.get_serializer_context())
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(transactions, many=True, context=self.get_serializer_context())
        return Response({
            "success": True,
            "transactions": serializer.data
        }, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path=r'get/(?P<transaction_id>\w+)')
    def get_transaction(self, request, transaction_id=None, *args, **kwargs):

        if transaction_id is None:
            raise ValidationError(self.missing_id_message)

        try:
            obj = Transaction.objects.get(pk=transaction_id)
        except ObjectDoesNotExist:
            raise NotFound(self.not_found_message)

        serializer = self.get_serializer(obj)

        return Response({
            "success": True,
            "transaction": serializer.data
        }, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='create')
    def create_transaction(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "success": True
        }, status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False, url_path=r'edit/(?P<transaction_id>\w+)')
    def edit_transaction(self, request, transaction_id=None, *args, **kwargs):

        if transaction_id is None:
            raise ValidationError(self.missing_id_message)

        try:
            obj = Transaction.objects.get(pk=transaction_id)
        except ObjectDoesNotExist:
            raise NotFound(self.not_found_message)

        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(obj, "_prefetched_objects_cache", None):
            obj._prefetched_objects_cache = {}

        return Response({
            "success": True
        }, status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path=r'delete/(?P<transaction_id>\w+)')
    def delete_transaction(self, request, transaction_id=None, *args, **kwargs):

        if transaction_id is None:
            raise ValidationError(self.missing_id_message)

        try:
            obj = Transaction.objects.get(pk=transaction_id)
        except ObjectDoesNotExist:
            raise NotFound(self.not_found_message)

        obj.delete()

        return Response({
            "success": True
        }, status.HTTP_200_OK)


