from Remetente import Remetente

if __name__ == "__main__":
    remetente = Remetente("azure-teste-namespace")
    status = remetente.enviar_mensagem({'Id': 'Value', 'color': 'blue', 'UF': 'BA'})
    print(status)
