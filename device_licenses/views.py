from netbox.views import generic
from . import forms, models, tables
from django.db.models import F
from datetime import date

class ContractView(generic.ObjectView):
    queryset = models.Contract.objects.all()

    def get_extra_context(self, request, instance):
        other_contracts = models.Contract.objects.filter(device__pk=instance.device.pk).exclude(pk=instance.pk)
        other_contracts_table = tables.ContractTableMinimal(other_contracts)

        return {
            'other_contracts_table': other_contracts_table,
        }

class ContractListView(generic.ObjectListView):
    queryset = models.Contract.objects.all()
    table = tables.ContractTable

class ContractEditView(generic.ObjectEditView):
    queryset = models.Contract.objects.all()
    form = forms.ContractForm

class ContractDeleteView(generic.ObjectDeleteView):
    queryset = models.Contract.objects.all()

class ContractBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Contract.objects.all()
    table = tables.ContractTable

class ContractTypeView(generic.ObjectView):
    queryset = models.ContractType.objects.all()

class ContractTypeListView(generic.ObjectListView):
    queryset = models.ContractType.objects.all()
    table = tables.ContractTypeTable

class ContractTypeEditView(generic.ObjectEditView):
    queryset = models.ContractType.objects.all()
    form = forms.ContractTypeForm

class ContractTypeDeleteView(generic.ObjectDeleteView):
    queryset = models.ContractType.objects.all()

class ContractTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ContractType.objects.all()
    table = tables.ContractTypeTable