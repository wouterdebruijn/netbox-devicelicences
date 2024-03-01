from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

from .jobs import sync_with_fortinet
from django_rq import get_queue
from django.http import HttpResponse

def fortisync_queue(request):
    # Register the job with django-rq
    queue = get_queue('default')
    queue.enqueue(sync_with_fortinet)
    return HttpResponse('Job enqueued')

urlpatterns = [
    path('contracts/', views.ContractListView.as_view(), name='contract_list'),
    path('contracts/<int:pk>/', views.ContractView.as_view(), name='contract'),
    path('contracts/add/', views.ContractEditView.as_view(), name='contract_add'),
    path('contracts/<int:pk>/edit/', views.ContractEditView.as_view(), name='contract_edit'),
    path('contracts/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract_delete'),
    path('contracts/bulkdelete/', views.ContractBulkDeleteView.as_view(), name='contract_bulk_delete'),
    path('contracts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='contract_changelog', kwargs={'model': models.Contract}),
    path('contracttypes/', views.ContractTypeListView.as_view(), name='contracttype_list'),
    path('contracttypes/<int:pk>/', views.ContractTypeView.as_view(), name='contracttype'),
    path('contracttypes/add/', views.ContractTypeEditView.as_view(), name='contracttype_add'),
    path('contracttypes/<int:pk>/edit/', views.ContractTypeEditView.as_view(), name='contracttype_edit'),
    path('contracttypes/<int:pk>/delete/', views.ContractTypeDeleteView.as_view(), name='contracttype_delete'),
    path('contracttypes/bulkdelete/', views.ContractTypeBulkDeleteView.as_view(), name='contracttype_bulk_delete'),
    path('contracttypes/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='contracttype_changelog', kwargs={'model': models.ContractType}),

    path('fortisync/', fortisync_queue, name='fortisync'),
]