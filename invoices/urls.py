from django.urls import path, include
from .routers import SlashOptionalRouter



from .invoice_views import  InvoiceViewSet
from .person_views import PersonViewSet

router = SlashOptionalRouter()

router.register(r'invoices', InvoiceViewSet)
router.register(r"persons", PersonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
