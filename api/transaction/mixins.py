from rest_framework.permissions import IsAuthenticated

from api.transaction.serializers import TransactionSerializer


class TransactionsMixin:
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    error_message = {"success": False, "msg": "Error updating transaction"}
