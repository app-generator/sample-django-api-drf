from api.transaction.models import Transaction
from datetime import datetime

data_transaction = {
    "product": "Fruit",
    "price": 20,
    "qty": 2,
    "discount": 5,
    "info": "Some fruits",
    "created_at": datetime.now()
}

Transaction.objects.create(**data_transaction)
