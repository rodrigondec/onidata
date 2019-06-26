from rest_framework_extensions.routers import ExtendedSimpleRouter

from users.views import UserViewSet
from contracts.views import ContractReadViewSet
from payments.views import PaymentReadViewSet


router = ExtendedSimpleRouter()

user_router = router.register(r'users', UserViewSet, basename='user')
user_router.register(r'contracts',
                     ContractReadViewSet,
                     basename='users-contracts',
                     parents_query_lookups=['user'])
user_router.register(r'payments',
                     PaymentReadViewSet,
                     basename='users-payments',
                     parents_query_lookups=['contract__user'])


urlpatterns = router.urls
