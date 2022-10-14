from Destinatario import Destinatario

if __name__ == "__main__":
    destinatario = Destinatario("azure-teste-namespace")
    mensage = destinatario.ler_mensagem()
    print(mensage)


