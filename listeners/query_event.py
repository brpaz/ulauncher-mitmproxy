from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """

        if not extension.get_mitmproxy_client().is_installed():
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Mitmweb was not found on your system',
                    description='Press enter to open the mitmproxy website',
                    highlightable=False,
                    on_enter=OpenUrlAction("https://mitmproxy.org/"))
            ])

        return extension.show_options()
