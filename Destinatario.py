from configServiceBus import ConfigServiceBus

class Destinatario:


    def __init__(self,queue_name):
        self.config = ConfigServiceBus()
        self.queue_name = queue_name
        self.received = self.config.get_client().get_queue_receiver(self.queue_name)

    def ler_mensagem(self):
        mensage = self.received.receive_messages(max_message_count=1)
        return mensage

