from gi.repository import Gio, GLib

SYSTEM_PROXY_SCHEMA = 'org.gnome.system.proxy'
SYSTEM_PROXY_MODE_KEY = 'mode'
PROXY_CONFIG_SCHEMA_HTTP = 'org.gnome.system.proxy.http'
PROXY_CONFIG_SCHEMA_HTTPS = 'org.gnome.system.proxy.https'
PROXY_CONFIG_HOST_KEY = 'host'
PROXY_CONFIG_HOST_PORT = "port"


class SystemProxyManager(object):
    """ Manages the system proxy activatation and deactivation"""

    def enable(self, port):
        """ Enables the system to use the new proxy config"""
        gsettings = Gio.Settings.new(PROXY_CONFIG_SCHEMA_HTTP)
        gsettings.set_value(PROXY_CONFIG_HOST_KEY,
                            GLib.Variant("s", "localhost"))
        gsettings.set_value(PROXY_CONFIG_HOST_PORT,
                            GLib.Variant("i", int(port)))

        gsettings = Gio.Settings.new(PROXY_CONFIG_SCHEMA_HTTPS)
        gsettings.set_value(PROXY_CONFIG_HOST_KEY,
                            GLib.Variant("s", "localhost"))
        gsettings.set_value(PROXY_CONFIG_HOST_PORT,
                            GLib.Variant("i", int(port)))

        gsettings = Gio.Settings.new(SYSTEM_PROXY_SCHEMA)
        gsettings.set_value(SYSTEM_PROXY_MODE_KEY, GLib.Variant("s", "manual"))

    def disable(self):
        """ Enables the system to use the new proxy config"""
        gsettings = Gio.Settings.new(SYSTEM_PROXY_SCHEMA)
        gsettings.set_value(SYSTEM_PROXY_MODE_KEY, GLib.Variant("s", "none"))
