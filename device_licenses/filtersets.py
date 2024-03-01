from netbox.filtersets import NetBoxModelFilterSet
from .models import Contract, ContractType

class ContractFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = Contract
        fields = ['id', 'contract_number', 'device', 'type', 'sku', 'start_date', 'end_date', 'origin']

class ContractTypeFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = ContractType
        fields = ['id', 'manufacturer', 'type', 'comments']



