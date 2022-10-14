from azure.servicebus import ServiceBusClient

class ConfigServiceBus:

    def __init__(self):
        self.CONNECTION_STR = 'Endpoint=sb://azure-teste-namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=2x+BQ7CsJkev68jo0DbGaWj9gYmh5l5OwNH1k+OcKZg='
        self.client = ServiceBusClient.from_connection_string(self.CONNECTION_STR)

    def get_client(self):
        return self.client

