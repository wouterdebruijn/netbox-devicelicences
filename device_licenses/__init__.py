from extras.plugins import PluginConfig
from django_rq import get_queue

class DeviceLicensesConfig(PluginConfig):
    name = 'device_licenses'
    verbose_name = 'Device Licenses'
    description = 'Manage devices licenses and (support) contracts'
    version = '0.1'
    author = 'Wouter de Bruijn'
    author_email = 'wouter@netco.nl'
    base_url = 'device-licenses'
    queues = ['default']

config = DeviceLicensesConfig

def ready(self):
    enqueue_jobs()


def enqueue_jobs():
    queue = get_queue('device_licenses.default')
    from .jobs import device_contracts_job
    queue.enqueue(device_contracts_job)
    print('Enqueued device_contracts_job')
