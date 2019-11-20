# -*- coding: utf-8 -*-

print('PROBLEMA #1: MISSIONÁRIOS E CANIBAIS')
print('\n' + 'O objetivo é passar todos os integrantes de um lado ao outro do rio, obedecendo as restrições.')
print('\n' + 'Restrições:')
print('-Máximo de duas pessoas no barco, além do barqueiro.')
print('-A quantidade de canibais não deve ser superior à de missionários em um lado do rio.' + '\n')
print('OBS: Qualquer estado que não obedeça as restrições será REJEITADO.' + '\n')
print('Descrição do estado: [a, b, c, d, e, f]')
print('a = quantidade de missionários no lado 1')
print('b = quantidade de canibais no lado 1')
print('c = quando 1, significa que barco está no lado 1')
print('d = quantidade de missionários no lado 2')
print('e = quantidade de canibais no lado 2')
print('f = quando 1, significa que barco está no lado 2')
print('\n' + '----------------------------------------------' + '\n')

visitados = [0]*331001  # marca com 1 os estados já visitados para evitar repetição
fronteira = []  # contém todos os estados válidos a serem analisados

inicio = [3, 3, 1, 0, 0, 0] # estado inicial

print('Iniciando BUSCA EM LARGURA.' + '\n')
print('Adicionando nó inicial ', inicio, ' à fronteira.' + '\n')
fronteira.append(inicio)

i = 0   # índice que marca a posição do estado atual na fronteira

# verifica validade do estado gerado
def verificar_filho(filho, posicao):

    # verifica condição de quantidade (mais canibais que missionários)
    if (filho[0] != 0 and filho[0] < filho[1]) or (filho[3] != 0 and filho[3] < filho[4]):
        print(filho, 'Estado REJEITADO.')
        filho = fronteira[i][:]
        return filho

    # verifica quantidades negativas
    for j in range(0, len(filho)):
        if filho[j] < 0:
            print(filho, 'Estado REJEITADO.')
            filho = fronteira[i][:]
            return filho
    
    # move o barco dependendo de que lado ele está
    if posicao == 0:
        filho[2] = 0; filho[5] = 1
    else:
        filho[2] = 1; filho[5] = 0

    # adiciona estado válido para verificação futura
    fronteira.append(filho[:])
    print(filho, 'Estado ADICIONADO à fronteira.')
    filho = fronteira[i][:]
    return filho

# método operador
def mover(posicao):
    
    filho = fronteira[i][:]
    print('Nó atual ', filho, ' não é o objetivo.')
    print('\n' + 'Aplicando operadores em nó atual...')
    
    if posicao == 0:
        a = 1; x = 0; y = 3; z = 4
    else:
        a = 4; x = 3; y = 0; z = 1
    
    # dois missionários
    print('\n' + 'Filho #1:', end=' ')
    filho[x] = fronteira[i][x] - 2
    filho[y] = fronteira[i][y] + 2
    filho = verificar_filho(filho, posicao)

    # dois canibais
    print('Filho #2:', end=' ')
    filho[a] = fronteira[i][a] - 2
    filho[z] = fronteira[i][z] + 2
    filho = verificar_filho(filho, posicao)

    # um missionário e um canibal
    print('Filho #3:', end=' ')
    filho[x] = fronteira[i][x] - 1
    filho[a] = fronteira[i][a] - 1
    filho[y] = fronteira[i][y] + 1
    filho[z] = fronteira[i][z] + 1
    filho = verificar_filho(filho, posicao)

    # um missionário
    print('Filho #4:', end=' ')
    filho[x] = fronteira[i][x] - 1
    filho[y] = fronteira[i][y] + 1
    filho = verificar_filho(filho, posicao)

    # um canibal
    print('Filho #5:', end=' ')
    filho[a] = fronteira[i][a] - 1
    filho[z] = fronteira[i][z] + 1
    filho = verificar_filho(filho, posicao)

    print('\n'+ '----------------------------------------------' + '\n')

    return

def foi_visitado():

    estado = int(str(fronteira[i][0])
               + str(fronteira[i][1])
               + str(fronteira[i][2])
               + str(fronteira[i][3])
               + str(fronteira[i][4])
               + str(fronteira[i][5]))
    
    if visitados[estado] == 1:
        return True
    else:
        visitados[estado] = 1
        return False

# MAIN

while(fronteira[i][3] + fronteira[i][4] != 6): # enquanto não for objetivo

    if not foi_visitado():  # verifica se estado já foi visitado
        
        print('Pegando próximo nó da fronteira ainda não visitado...')
        if fronteira[i][2] == 1:    # verifica se o barco está no lado 1
            mover(0)
        else:
            mover(1)
    
    i+=1

print('Pegando próximo nó da fronteira ainda não visitado...')
print('Nó atual ', fronteira[i], ' é o objetivo. Busca encerrada.')
