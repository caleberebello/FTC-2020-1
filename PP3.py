fita1 = list(input())
fita1.insert(0, 'B')
fita1.append('B')
fita2 = ['B'] * len(fita1)
fita3 = ['B'] * len(fita1)
for i in range(200):
        fita1.append('B')
        fita2.append('B')
        fita3.append('B')
cab1 = 1
cab2 = 1
cab3 = 1


def q0():
    global cab1, cab2, cab3
    while (fita1[cab1] == 'I' and fita2[cab2] == 'B' and fita3[cab3] == 'B'):
        cab1 += 1
        fita2[cab2] = 'I'
        cab2 += 1
    if (fita1[cab1] == '#' and fita2[cab2] == 'B' and fita3[cab3] == 'B'):
        cab1 += 1
        q1()
    else:
        rejeita()


def q1():
    global cab1, cab2, cab3
    if (fita1[cab1] == '#'):
            rejeita()
    while (fita1[cab1] == 'I' and fita2[cab2] == 'B' and fita3[cab3] == 'B'):
        cab1 += 1
        fita3[cab3] = 'I'
        cab3 += 1
        if (fita1[cab1] == '#'):
            rejeita()
    if (fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'B'):
        cab2 -= 1
        cab3 -= 1
        q2()


def q2():
    global cab1, cab2, cab3
    while (fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'I'):
        cab2 -= 1
        cab3 -= 1

    if (fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'I'):
        fita1[cab1] = '='
        cab1 += 1
        cab2 += 1
        q3()
    elif ((fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'B') or (fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'B')):
        if(fita2[cab2] == 'B'):
            cab2 += 1
            cab3 += 1
            q4()
        elif (fita2[cab2] == 'I'):
            cab2 -= 1
            cab3 += 1
            q4()


def q3():
    global cab1, cab2, cab3
    while (fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'I'):
        fita1[cab1] = 'I'
        cab1 += 1
        fita2[cab2] = 'B'
        cab2 += 1

    if(fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'I'):
        q9()


def q4():
    global cab1, cab2, cab3
    while (fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'I'):
        cab2 -= 1
    if (fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'I'):
        cab2 += 1
        q5()


def q5():
    global cab1, cab2, cab3
    while (fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'I'):
        fita2[cab2] = 'B'
        cab2 += 1
        cab3 += 1
    if(fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'B'):
        cab3 -= 1
        q6()
    elif(fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'I'):
        fita3[cab3] = 'B'
        cab3 += 1
        q7()


def q6():
    global cab1, cab2, cab3
    while (fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'I'):
        cab3 -= 1
    if (fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'B'):
        cab3 += 1
        q5()


def q7():
    global cab1, cab2, cab3
    while ((fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'I') or (fita1[cab1] == 'B' and fita2[cab2] == 'I' and fita3[cab3] == 'I')):
        if(fita2[cab2] == 'B'):
            fita3[cab3] = 'B'
            cab3 += 1
        elif(fita2[cab2] == 'I'):
            cab3 -= 1
    if(fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'B'):
        fita1[cab1] = '='
        cab1 += 1
        cab3 -= 1
        q8()


def q8():
    global cab1, cab2, cab3
    while((fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'I') or (fita1[cab1] == 'B' and fita2[cab2] == 'B' and fita3[cab3] == 'B')):
        if (fita3[cab3] == 'I'):
            fita1[cab1] = 'I'
            cab1 += 1
            fita2[cab2] = 'x'
            cab2 += 1

            fita3[cab3] = 'B'
            cab3 -= 1
        elif(fita3[cab3] == 'B'):
            cab2 -= 1
            cab3 -= 1
        if(fita1[cab1] == 'B' and fita2[cab2] == 'x' and fita3[cab3] == 'B'):
            q9()


def q9():
    global cab1
    for i in range(1, cab1):
        print(fita1[i], end='')
    print(' ACEITA')


def rejeita():
    for i in range(1, len(fita1)):
        if( (fita1[i] == 'I') or (fita1[i] == '#') ):
            print(fita1[i], end='')
    print(' REJEITA')

q0()