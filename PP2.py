def verifica(e, d, entrada):
    pilha = ['$']
    for i in entrada:
        if (i == e):
            pilha.append(e)
        elif (i == d):
            if(e in pilha):
                pilha.pop()
            else:
                pilha.append('0')

    if pilha[-1] != '$':
        return 0
    else:
        return 1


def ecasada(entrada):
    R = 0
    if verifica('(', ')', entrada) and verifica('[', ']', entrada) and verifica('{', '}', entrada):
        R = 1
    return R


def ecorreta(entrada, result):

    pilha = ['$']
    topo = pilha[-1]
    if(ecasada(entrada)):
        for i in entrada:
            topo = pilha[-1]
            if(i == '{'):
                if(topo == '[' or topo == '('):
                    pilha.append('0')
                else:
                    pilha.append('{')
            elif(i == '}' and (topo == '{')):
                pilha.pop()

            if (i == '['):
                if(topo == '('):
                    pilha.append('0')
                else:
                    pilha.append('[')
            elif (i == ']' and topo == '['):
                pilha.pop()

            if (i == '('):
                pilha.append('(')
            elif (i == ')' and topo == '('):
                pilha.pop()
        if (pilha[-1] != '$'):
            result.append('casada e incorreta')
        else:
            result.append('casada e correta')
    else:
        result.append('nao casada')
    return result


def correcao(entrada, correcoes):
    entrada = list(entrada)
    aux = []
    
    ecorreta(entrada, aux)
    if(aux[0] == 'casada e incorreta'):
        while(aux[0] != 'casada e correta'):
            for c, i in enumerate(entrada):
                if(i == '(' and entrada[c + 1] == '['):
                    entrada[c] = '['
                    entrada[c + 1] = '('

                elif(i == '(' and entrada[c + 1] == '{'):
                    entrada[c] = '{'
                    entrada[c + 1] = '('

                elif(i == '[' and entrada[c + 1] == '{'):
                    entrada[c] = '{'
                    entrada[c + 1] = '['

                elif(i == ')' and entrada[c - 1] == '}'):
                    entrada[c] = '}'
                    entrada[c - 1] = ')'

                elif(i == ')' and entrada[c - 1] == ']'):
                    entrada[c] = ']'
                    entrada[c - 1] = ')'
                elif(i == ']' and entrada[c - 1] == '}'):
                    entrada[c] = '}'
                    entrada[c - 1] = ']'
                elif(i == ' '):
                    entrada.remove(' ')
            aux = []
            ecorreta(entrada, aux)
            if(aux[0] == 'casada e correta'):
                correcoes.append(entrada)
    return correcoes

result = []
correcoes = []
vazio = ""
entrada = str

while(entrada != vazio):
    if (entrada != vazio):
        entrada = (input())
        if (entrada != vazio):
            ecorreta(entrada, result)
            correcao(entrada, correcoes)
for i in result:
    print(i)

for i in correcoes:
    for j in i:
        print(j, end='')
    print()