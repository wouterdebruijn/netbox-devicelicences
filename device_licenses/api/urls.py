from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'device_licenses'

router = NetBoxRouter()
router.register('contracts', views.ContractViewSet)
router.register('contracttypes', views.ContractTypeViewSet)

urlpatterns = router.urls