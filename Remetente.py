from azure.servicebus import ServiceBusMessage
from configServiceBus import ConfigServiceBus

class Remetente:


    def __init__(self,queue_name):
        self.config = ConfigServiceBus()
        self.queue_name = queue_name
        self.sender = self.config.get_client().get_queue_sender(self.queue_name)


    def enviar_mensagem(self,conteudo):
        try:
            mensage = ServiceBusMessage(str(conteudo))
            self.sender.send_messages(mensage)
            return True
        except Exception as ex:
            print(ex)
            return False
