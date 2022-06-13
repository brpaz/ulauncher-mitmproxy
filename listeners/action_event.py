from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

from mitmproxy.exceptions import ProxyIsAlreadyRunningError

ACTION_START = "start"
ACTION_STOP = "stop"
ACTION_STATUS = "status"


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()

        if data["action"] == ACTION_START:
            return self.handle_proxy_start(extension)

        if data["action"] == ACTION_STOP:
            return self.handle_proxy_stop(extension)

        if data["action"] == ACTION_STATUS:
            return self.handle_tatus(extension)

    def handle_tatus(self, extension):
        running = extension.get_mitmproxy_client().is_running()

        message = "Proxy stopped"
        if running:
            message = "Proxy is running"

        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name=message,
                                description='Starts Mitmproxy server',
                                highlightable=False,
                                on_enter=HideWindowAction())
        ])

    def handle_proxy_start(self, extension):
        """ Starts the mitmweb server"""
        try:
            prefs = extension.preferences
            extension.get_mitmproxy_client().start(prefs["proxy_port"],
                                                   prefs["web_port"])

            if prefs["manage_system_proxy"] == "true":
                extension.get_system_proxy_manager().enable(
                    prefs["proxy_port"])

            extension.show_notification("MitmProxy started on port %s" %
                                        prefs["proxy_port"])

            return OpenUrlAction("http://localhost:{}".format(
                prefs["web_port"]))

        except ProxyIsAlreadyRunningError:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Error: An mitmweb instance is already running.',
                    description='Press enter to open mitmweb in your default browser',
                    highlightable=False,
                    on_enter=OpenUrlAction("http://localhost:{}".format(
                        prefs["web_port"])))
            ])
        except Exception as e:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=str(e),
                    description='An error occurred while starting mitmweb server',
                    highlightable=False,
                    on_enter=HideWindowAction())
            ])

    def handle_proxy_stop(self, extension):
        """ Stops the mitmweb server"""

        try:
            extension.get_mitmproxy_client().stop()

            extension.show_notification("MitmProxy stopped")
            return HideWindowAction()
        except Exception as e:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=str(e),
                    description='An error occurred while stopping mitmweb server',
                    highlightable=False,
                    on_enter=HideWindowAction())
            ])
        finally:
            if extension.preferences["manage_system_proxy"] == "true":
                extension.get_system_proxy_manager().disable()
