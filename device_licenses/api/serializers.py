from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Contract, ContractType

class ContractSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:device_licenses-api:contract-detail')
    
    class Meta:
        model = Contract
        fields = ['id', 'contract_number', 'sku', 'device', 'comments', 'start_date', 'end_date', 'type', 'origin', 'expiration', 'expired', 'url']

class ContractTypeSerializer(NetBoxModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:device_licenses-api:contracttype-detail')
    
    class Meta:
        model = ContractType
        fields = ['id', 'manufacturer', 'type', 'comments', 'url']