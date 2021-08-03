from rest_framework import routers

from api.transaction.viewsets import (TransactionViewSetCreate, TransactionViewSetDelete, TransactionViewSetList, TransactionViewSetRetrieve, TransactionViewSetUpdate)

router = routers.SimpleRouter(trailing_slash=False)

router.register('create', TransactionViewSetCreate, basename="transaction-create")

router.register('get', viewset=TransactionViewSetList, basename="transactions-get")

router.register('delete', viewset=TransactionViewSetDelete, basename="transaction-delete")

router.register('edit', viewset=TransactionViewSetUpdate, basename="transaction-delete")

urlpatterns = [
    *router.urls,
]
