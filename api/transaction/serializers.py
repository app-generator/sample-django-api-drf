from api.transaction.models import Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    info = serializers.CharField(allow_null=True, allow_blank=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Transaction
        fields = ["id", "product", "price", "qty", "discount", "info", "created_at"]
        read_only_field = ["id", "created_at"]
