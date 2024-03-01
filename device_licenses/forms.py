from netbox.forms import NetBoxModelForm
from .models import Contract, ContractType

class ContractForm(NetBoxModelForm):
    
    class Meta:
        model = Contract
        fields = [
            'contract_number',
            'sku',
            'device',
            'comments',
            'start_date',
            'end_date',
            'type',
            'origin'
        ]

class ContractTypeForm(NetBoxModelForm):
        
    class Meta:
        model = ContractType
        fields = ['manufacturer', 'type', 'comments']