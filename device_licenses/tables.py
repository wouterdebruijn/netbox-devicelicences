import django_tables2 as tables

from netbox.tables import NetBoxTable
from .models import Contract, ContractType
from django_tables2.utils import A

class ContractTable(NetBoxTable):
    contract_number = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    type = tables.Column(linkify=True)

    expiration = tables.Column(verbose_name='Expiration', accessor=A('expiration'), order_by='end_date')

    # Render a badge for the active_terms column, depending on the value
    def render_expiration(self, value):
        return Contract.render_expiration_by_value(value)

    class Meta(NetBoxTable.Meta):
        model = Contract
        fields = ('pk', 'id', 'contract_number', 'sku', 'device', 'comments', 'expiration', 'type', 'origin', 'start_date', 'end_date')
        default_columns = ('contract_number', 'type', 'expiration', 'device', 'end_date')

# Minimal table for the device detail view listing the contracts for a device
class ContractTableMinimal(ContractTable):
    contract_number = tables.Column(linkify=True)
    type = tables.Column(linkify=True)

    class Meta(ContractTable.Meta):
        fields = ('pk', 'id', 'contract_number', 'sku', 'device', 'comments', 'expiration', 'type', 'origin', 'start_date', 'end_date')
        default_columns = ('contract_number', 'type', 'expiration', 'end_date')
        order_by = ('-expiration',)

class ContractTypeTable(NetBoxTable):
    type = tables.Column(linkify=True)
    manufacturer = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = ContractType
        fields = ('pk', 'id', 'type', 'manufacturer', 'comments')
        default_columns = ('type', 'manufacturer', 'comments')