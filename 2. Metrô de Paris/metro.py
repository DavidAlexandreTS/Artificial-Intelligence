# -*- coding: utf-8 -*-

print('PROBLEMA #2: METRÔ DE PARIS')
print('\n' + 'O objetivo é apresentar ao usuário o menor caminho entre a estação inicial e o seu destino.')
print('\n' + 'Informações importantes:')
print('-Velocidade média do metrô: 30km/h')
print('-Tempo de baldeação: 4 minutos')
print('-O problema recebe apenas inteiros como entrada' + '\n')

duracao =  [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
			(0, 0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32),
			(0, 11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24),
			(0, 20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18),
			(0, 27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17),
			(0, 40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20),
			(0, 43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20),
			(0, 39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17),
			(0, 28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30),
			(0, 18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28),
			(0, 10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23),
			(0, 18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 0, 15, 35, 39),
			(0, 30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37),
			(0, 30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5),
			(0, 32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 0)]

conexao =  [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
			(0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
			(0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0),
			(0, 0, 1, 0, 1, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0),
			(0, 0, 0, 1, 0, 1, 0, 0, 3, 0, 0, 0, 0, 3, 0),
			(0, 0, 0, 0, 1, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0),
			(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
			(0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
			(0, 0, 0, 0, 3, 2, 0, 0, 0, 2, 0, 0, 3, 0, 0),
			(0, 0, 2, 4, 0, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0),
			(0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
			(0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0),
			(0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0),
			(0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3),
			(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0)]

# CODIGO DE CORES PARA LINHAS DO METRÔ:
# azul = 1
# amarelo = 2
# verde = 3
# vermelho = 4

fronteira = []
caminho = []
velocidade_media = 30
custo_de_troca = 4 / 60

# converte distância (km) em tempo (h)
duracao[:] = [[round(distancia / velocidade_media, 2) for distancia in x] for x in duracao]

def cor(id):
	if id == 1:
		return 'azul'
	if id == 2:
		return 'amarela'
	if id == 3:
		return 'verde'
	else:
		return 'vermelha'

# método para inserção de estado ordenado por f(n) na fronteira
def insertion_sort(estado):
	i = 0
	
	while i < len(fronteira) and estado[2] >= fronteira[i][2]:
		i = i+1
	fronteira.insert(i, estado)

# método de impressão de caminho
def exibir_caminho():
	print('\n' + 'Caminho apresentado pelo Algoritmo A*:')
	print('\n' + 'Iniciando viagem da Estação', estado_inicial, 'com destino à Estação', estado_final, '...\n')
	caminho.pop(0)

	linha = caminho[0][4]
	tempo = 0

	for estado in caminho:
		if estado[4] != linha:
			print('Mude para a linha ', cor(estado[4]), '(tempo de espera: 4 minutos)')

		print('Siga para a Estação ', estado[0], 'pela linha', cor(estado[4]))
		linha = estado[4]
		tempo = estado[3]
	print('\nTempo total de viagem:', round(tempo, 2), 'hora(s).')
	return

# verifica mudança de linha
def verificar_estacao(estado):
	if estado[1][4] != 0 and estado[1][4] != estado[4]:
		return custo_de_troca
	return 0

def verificar_objetivo(estado):
	if estado[0] == estado_final:	# se chegou ao estado final, recupera caminho até ele
		while estado[1] != None:
			caminho.insert(0, estado)
			estado = estado[1]
		caminho.insert(0, estado)
		return True
	return False

def gerar_filhos(estado):

	filho = []

	if not verificar_objetivo(estado): # se não for estado final, gera sucessores
		for i in range(len(conexao[0])):
			if conexao[estado[0]][i] != 0:	# se existir conexão entre as estações, e a estação não for seu pai, gera
				if estado[1] != None:
					if estado[1][0] != i:
						filho = [i, estado, 0, estado[3] + duracao[estado[0]][i], conexao[estado[0]][i]]
						filho[2] = avaliacao(filho)
						filho[3] += verificar_estacao(filho)
						insertion_sort(filho)
				else:
					filho = [i, estado, 0, estado[3] + duracao[estado[0]][i], conexao[estado[0]][i]]
					filho[2] = avaliacao(filho)
					insertion_sort(filho)
		return True
	else:	# se for objetivo, imprime caminho
		exibir_caminho()
	return False

# método que calcula função de avaliação f(n)
def avaliacao(estado):
	if estado[1] != None:	# se estado tiver pai, verifica condição de monotonicidade da função de avaliação
		# max entre f(n) do pai e g(n) + h(n) do filho
		return max(estado[1][2], estado[3] + duracao[estado[0]][estado_final])
	return estado[3] + duracao[estado[0]][estado_final]

# MAIN

estado_inicial = int(input('Em que estação você se encontra? '))
estado_final = int(input('Para qual estação deseja ir? '))

# estado = [id do estado atual, ponteiro para seu pai, f(n), g(n), linha]
# f(n) é usado para ordenar os estados na lista
# g(n) é usado para incrementar custo no filho
estado_atual = [estado_inicial, None, 0, 0, 0]
estado_atual[2] = avaliacao(estado_atual)
fronteira.append(estado_atual)

gerar_filhos(estado_atual)

while gerar_filhos(estado_atual):
	fronteira.pop(0)
	estado_atual = fronteira[0]
