from rest_framework import routers

from api.transaction.viewsets import (TransactionViewSetCreate, TransactionViewSetDelete, TransactionViewSetList, TransactionViewSetRetrieve, TransactionViewSetUpdate)

router = routers.SimpleRouter(trailing_slash=False)

router.register('create', TransactionViewSetCreate, basename="transaction-create")

urlpatterns = [
    *router.urls,
]
