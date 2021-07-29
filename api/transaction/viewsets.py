from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import MethodNotAllowed

from api.transaction.mixins import TransactionsMixin
from api.transaction.models import Transaction


class TransactionViewSetCreate(viewsets.GenericViewSet, mixins.CreateModelMixin, TransactionsMixin):
    pass


class TransactionViewSetDelete(viewsets.GenericViewSet, mixins.DestroyModelMixin, TransactionsMixin):
    pass


class TransactionViewSetUpdate(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, TransactionsMixin):

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = Transaction.objects.get(id=request.data.get("transactionId"))
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        transaction_id = request.data.get("transactionId")

        if not transaction_id:
            raise ValidationError(self.error_message)

        if not self.request.user.is_superuser:
            raise ValidationError(self.error_message)

        self.update(request)

        return Response({"success": True}, status.HTTP_200_OK)


class TransactionViewSetList(viewsets.GenericViewSet, mixins.ListModelMixin, TransactionsMixin):

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Transaction.objects.all()
        raise MethodNotAllowed('GET')


class TransactionViewSetRetrieve(viewsets.GenericViewSet, mixins.RetrieveModelMixin, TransactionsMixin):
    pass
