from extras.plugins import PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:device_licenses:contract_list',
        link_text='Device Contracts',
        buttons=(
            PluginMenuButton(
                link='plugins:device_licenses:contract_add',
                title='Add Contract',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:device_licenses:contracttype_list',
        link_text='Contract Types',
        buttons=(
            PluginMenuButton(
                link='plugins:device_licenses:contracttype_add',
                title='Add Device Contract Type',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            ),
        ),
    ),
)