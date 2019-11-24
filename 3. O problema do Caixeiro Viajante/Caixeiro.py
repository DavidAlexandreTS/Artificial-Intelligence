# -*- coding: utf-8 -*-
from random import randint

print('PROBLEMA #3: CAIXEIRO VIAJANTE')
print('\n' + 'O objetivo é apresentar o menor caminho para percorrer todas as cidades, retornando a cidade inicial.')
print('\n' + 'Informações importantes:')
print('-Estados filhos são gerados trocando-se duas cidades de lugar')
print('-O problema recebe apenas um inteiro como entrada, representando a cidade natal do caixeiro' + '\n')

distancia = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
			 (0, 0, 30, 84, 56, -1, -1, -1, 75, -1, 80),
			 (0, 30, 0, 65, -1, -1, -1, 70, -1, -1, 40),
			 (0, 84, 65, 0, 74, 52, 55, -1, 60, 143, 48),
			 (0, 56, -1, 74, 0, 135, -1, -1, 20, -1, -1),
			 (0, -1, -1, 52, 135, 0, 70, -1, 122, 98, 80),
			 (0, 70, -1, 55, -1, 70, 0, 63, -1, 82, 35),
			 (0, -1, 70, -1, -1, -1, 63, 0, -1, 120, 57),
			 (0, 75, -1, 135, 20, 122, -1, -1, 0, -1, -1),
			 (0, -1, -1, 143, -1, 98, 82, 120, -1, 0, -1),
			 (0, 80, 40, 48, -1, 80, 35, 57, -1, -1, 0)]

estado_inicial = [1, 2, 10, 6, 7, 9, 3, 4, 5, 8]
estado_final = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
custo_atual = 0
fronteira = []
limite = 0

# método que seta solução inicial para aplicar algoritmo
def setar_inicio(cidade_inicial):
	for i in range(len(estado_inicial)):
		if estado_inicial[i] == cidade_inicial:
			break
	for j in range(len(estado_final)):
		estado_final[j] = estado_inicial[i]
		i += 1
		if i == len(estado_inicial):
			i = 0

# método para verificar se caminho está conectado de acordo com matriz de distância
def verificar_caminho(estado):
	for i in range(len(estado)-1):
		if distancia[estado[i]][estado[i+1]] == -1:
			return False
	if distancia[estado[9]][estado[0]] == -1:
		return False
	else:
		return True

# método para calcular custo do caminho recebido
def calcular_custo(estado):
	custo = 0
	for i in range(len(estado)-1):
		custo += distancia[estado[i]][estado[i+1]]
	custo += distancia[estado[9]][estado[0]]
	return custo

# método que retonar permutação aleatória
def permutacao():
	a = b = 0
	while a == b:	
		a = randint(1, 9)
		b = randint(1, 9)
	return a,b

# método que gera 100000 sucessores baseado na permutação de duas cidades
def gerar_filhos(estado):
	i = 0
	filho = []
	qtd_valida = 0
	while i != 100000:
		filho = estado[:]
		a, b = permutacao()
		filho[a] = estado[b]
		filho[b] = estado[a]

		if verificar_caminho(filho):
			fronteira.append(filho)
			qtd_valida += 1
		i += 1
	print('----------------------------------------------' + '\n')
	print(qtd_valida, 'caminhos válidos foram gerados por permutação.')
	print('\n' + 'Verificando custo de soluções encontradas...' + '\n')

# MAIN

cidade = int(input('Em que cidade mora o caixeiro (número de 1 à 10)? '))
setar_inicio(cidade)
custo_atual = calcular_custo(estado_final)

print('\n' + 'Inciando busca com algoritmo de Subida da Encosta, partindo da solução:', estado_inicial)
print('Custo atual:', custo_atual, '\n')

while limite != 10:	# busca para após 10 tentativas sem melhora de custo
	gerar_filhos(estado_final)
	for i in range(len(fronteira)):
		custo = calcular_custo(fronteira[i])
		if custo < custo_atual:
			limite = 0
			estado_final = fronteira[i]
			custo_atual = custo
			print('Solução melhor encontrada!')
			print('Caminho:', estado_final)
			print('Custo:', custo_atual, '\n')
	del fronteira[:]
	limite += 1
	print('Se não for encontrada solução melhor, busca se encerrará em', 10-limite, 'tentativa(s).')

print('\n' + 'Busca encerrada!')
print('Solução final:')
print('Caminho:', estado_final)
print('Custo:', custo_atual)
