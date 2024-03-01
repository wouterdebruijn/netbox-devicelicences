from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import ContractSerializer, ContractTypeSerializer

class ContractViewSet(NetBoxModelViewSet):
    queryset = models.Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_class = filtersets.ContractFilterSet


class ContractTypeViewSet(NetBoxModelViewSet):
    queryset = models.ContractType.objects.all()
    serializer_class = ContractTypeSerializer
    filterset_class = filtersets.ContractTypeFilterSet