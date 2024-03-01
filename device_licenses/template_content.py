from extras.plugins import PluginTemplateExtension
from . import models, tables
from datetime import date

class DeviceLicenseCard(PluginTemplateExtension):
    # Add extra content to the device detail view
    model = 'dcim.device'

    def right_page(self):
        # Get all the contract terms for this device
        contracts = models.Contract.objects.filter(device=self.context['object'])

        # Render the card template with the generated table as extra context
        return self.render('device_licenses/card.html', extra_context={
            # We pass the request so that the table can be ordered by the user
            'contracts': tables.ContractTableMinimal(contracts, request=self.context['request']),
        })

template_extensions = [DeviceLicenseCard]