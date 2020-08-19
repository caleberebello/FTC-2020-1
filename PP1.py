import re

def beginmessage(bgm):
    if re.search(r'[-]{5}beginmessage[-]{5}',bgm):
        return True
    else:
        return False

def remetente(entrada):
    if re.search(r'from: [\w.-]+@[\w.-]+', entrada):
        return True
    else:
        return False

def destinatario(entrada):
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
    if re.search(r'[0-9]{4}.(0[1-9]|1[0-2]).(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]',entrada):
        separar = entrada.split(' ')
        ano, mes, dia = map(int, separar[0].split('.'))
        if mes < 1 or mes > 12 or ano <= 0:
            return False
        if mes in (1, 3, 5, 7, 8, 10, 12):
            ultimo_dia = 31
        elif mes == 2:
            if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                ultimo_dia = 29
            else:
                ultimo_dia = 28
        else:
            ultimo_dia = 30
        if dia < 1 or dia > ultimo_dia:
            return False
        return True
    else:
        return False

def separador(sp):
    if re.search(r'[-]{23}',sp):
        return True
    else:
        return False

def mensagem(entrada):
    match = re.search(r'\w{11,}',entrada)
    if re.search(r'[\w.-]+@[\w.-]+',entrada):
        return False
    elif re.search(r'<.+?>',entrada):
        return False
    elif re.search(r'milionário|empréstimo|loteria|banco|herança|seguidor|desconto',entrada):
        return False
    elif match:
        match.group()
        vogais = "aeiouAEIOU"
        vogal = 0
        consoante = 0
        for letra in match.group():
            if letra in vogais:
                vogal += 1
            else:
                consoante += 1
        if consoante > vogal:
            return False
        else:
            return True
    elif re.search(r'[.,;]{15,}',entrada):
        return False
    else:
        return True


entrada = input().strip("\r")
conteudo = open(entrada,'r')
bgm = conteudo.readline()
rem = conteudo.readline()
dest = conteudo.readline()
ip = conteudo.readline()
data_hora = conteudo.readline()
sp = conteudo.readline()
msg = conteudo.read()

vetor = [beginmessage(bgm),remetente(rem),destinatario(dest),verificar_IP(ip),timestamp(data_hora),separador(sp),mensagem(msg)]


if vetor == [True,True,True,True,True,True,True]:
    print("ham")
else:
    print("spam")