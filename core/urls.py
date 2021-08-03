from django.urls import path, include

urlpatterns = [
    path("api/users/", include(("api.routers.users", "api-users"), namespace="api-users")),
    path("api/transactions/", include(("api.routers.transactions", "api-transactions"), namespace="api-transactions"))
]
