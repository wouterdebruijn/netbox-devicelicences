# Example Response Path: ~/Downloads/fortinet_response.json
# import json file as body

try:
    from .models import Contract, ContractType
    from dcim.models import Device
except Exception as e:
    print(e)
    raise e

def device_contracts_job():
    print('device_contracts_job')

    for device in Device.objects.all():
        print(device)

def sync_with_fortinet():
    print('sync_with_fortinet')

    # Get all device objects from fortinet
    # with open('/Users/Wouter/Downloads/fortinet_response.json') as f:
    #     body = json.load(f)

    #     for asset in body['assets']:
    #         serial = asset['serialNumber']

    #         eor = asset['productModelEoR'].split('T')[0] if isinstance(asset['productModelEoR'], str) else None
    #         eos = asset['productModelEoS'].split('T')[0] if isinstance(asset['productModelEoS'], str) else None

    #         contracts = asset['contracts']

    #         # Get device object from NetBox
    #         try:
    #             device = Device.objects.get(serial=serial)
    #         except Device.DoesNotExist:
    #             continue

    #         print(f'Updating device {device.name}')

    #         # Update the netbox device with the correct eor and eol dates
    #         device.custom_field_data['model_eor'] = eor
    #         device.custom_field_data['model_eos'] = eos
    #         device.save()

    #         for contract in contracts:
    #             print("Contract on device loop")
    #             try:
    #                 existing_contract = Contract.objects.get(contract_number=contract['contractNumber'])
    #                 print(existing_contract)
    #             except Contract.DoesNotExist:
    #                 print("Creating new contract")
    #                 nb_contract = Contract()
    #                 nb_contract.contract_number = contract['contractNumber']
    #                 nb_contract.sku = contract['sku']
    #                 nb_contract.device = device
    #                 nb_contract.save()

    #                 for term in contract['terms']:
    #                     print("Creating new term in contract")
    #                     nb_term = ContractTerm()
    #                     nb_term.contract = nb_contract
    #                     nb_term.start_date = term['startDate'].split('T')[0] if isinstance(term['startDate'], str) else None
    #                     nb_term.end_date = term['endDate'].split('T')[0] if isinstance(term['endDate'], str) else None
    #                     nb_term.type = term['supportType']
    #                     nb_term.save()

