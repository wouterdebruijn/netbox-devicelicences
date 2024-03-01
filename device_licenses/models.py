from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse
from datetime import date
from django.utils.html import format_html

class Contract(NetBoxModel):
    contract_number = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, blank=True, null=True)
    device = models.ForeignKey('dcim.Device', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.ForeignKey('ContractType', on_delete=models.CASCADE)
    origin = models.CharField(max_length=50)

    class Meta:
        ordering = ['contract_number']

    def __str__(self):
        return self.contract_number
    
    def get_absolute_url(self):
        return reverse('plugins:device_licenses:contract', args=[self.pk])
    
    def expiration(self):
        return (self.end_date - date.today()).days
        
    def expired(self):
        return True if self.expiration() < 0 else False
    
    # Private method rendering a expiration badge
    def render_expiration(self):
        return self.render_expiration_by_value(self.expiration())
    
    # "Static" method rendering a expiration badge (used in tables.py)
    @staticmethod
    def render_expiration_by_value(value):
        if value < 0:
            return format_html(f'<span class="badge bg-red">Expired</span>')
        elif value < 30:
            return format_html(f'<span class="badge bg-orange">{value} day(s)</span>')
        else:
            return format_html(f'<span class="badge bg-green">{value} day(s)</span>')

class ContractType(NetBoxModel):
    manufacturer = models.ForeignKey('dcim.Manufacturer', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    comments = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ['manufacturer', 'type']

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('plugins:device_licenses:contracttype', args=[self.pk])