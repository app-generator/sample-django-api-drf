from rest_framework import routers

from api.transaction.viewsets import TransactionViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register('', TransactionViewSet, basename='transactions')

urlpatterns = [
    *router.urls,
]
