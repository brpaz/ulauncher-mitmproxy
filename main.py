""" Main Module """

import logging
import gi

from gi.repository import Notify
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from listeners.query_event import KeywordQueryEventListener
from listeners.action_event import ItemEnterEventListener
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from mitmproxy.client import Client
from utils.system_proxy import SystemProxyManager

gi.require_version('Notify', '0.7')

logger = logging.getLogger(__name__)


class MitmproxyExtension(Extension):
    """ Main Extension Class  """

    def __init__(self):
        """ Initializes the extension """
        super(MitmproxyExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.mitmproxy = Client()
        self.system_proxy_manager = SystemProxyManager()
        Notify.init("Ulauncher MitmProxy")

    def get_mitmproxy_client(self):
        return self.mitmproxy

    def get_system_proxy_manager(self):
        return self.system_proxy_manager

    def show_options(self):
        """ Render the extension main menu"""
        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name='Start ',
                                description='Starts Mitmproxy server',
                                highlightable=False,
                                on_enter=ExtensionCustomAction(
                                    {'action': 'start'}, keep_app_open=True)),
            ExtensionResultItem(icon='images/icon.png',
                                name='Stop',
                                description='Stops a running Mitmproxy server',
                                highlightable=False,
                                on_enter=ExtensionCustomAction(
                                    {'action': 'stop'}, keep_app_open=True)),
            ExtensionResultItem(
                icon='images/icon.png',
                name='Status',
                description='Checks the status of the Mitmproxy server',
                highlightable=False,
                on_enter=ExtensionCustomAction({'action': 'status'},
                                               keep_app_open=True))
        ])

    def show_notification(self, text):
        """
        Shows a notification
        Args:
          text (str): The text to display on the notification
        """
        Notify.Notification.new("Ulauncher MitmProxy", text).show()


if __name__ == '__main__':
    MitmproxyExtension().run()
