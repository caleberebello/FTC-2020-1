import re

def remetente(entrada):
    if re.search(r'from: [\w.-]+@[\w.-]+', entrada):
        return True
    else:
        return False

def destinatário(entrada):
    if re.search(r'to: [\w.-]+@[\w.-]+', entrada):
        return True
    else:
        return False

def verificar_IP(entrada):
    if re.search(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', entrada):
        return True
    else:
        return False

def timestamp(entrada):
    if re.search(r'[0-9]{4}.(0[1-9]|1[0-2]).(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]'):
        return True
    else:
        return False

entrada = input()
while entrada != '-----endmessage-----':
    if entrada != '-----beginmessage-----':
        print("spam")
    entrada = input()