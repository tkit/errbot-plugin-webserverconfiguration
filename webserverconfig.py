from errbot import BotPlugin, botcmd

class WebserverConfig(BotPlugin):
    """
    A plugin of webhook configuration
    """

    def get_configuration_template(self):
        return {
            'HOST': '0.0.0.0',
            'PORT': 3141,
            'SSL': {
                'enabled': False,
                'host': '0.0.0.0',
                'port': 3142,
                'certificate': "",
                'key': ""
            }
        }

    def configure(self, configuration=None):
        self.config = self.get_configuration_template()

    def activate(self):
        super().activate()
        self.other = self.get_plugin('Webserver')
        self.other.config = self.config
        self.other.activate()
