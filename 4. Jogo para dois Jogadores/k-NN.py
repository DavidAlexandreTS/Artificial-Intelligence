import math
import heapq
import random

def classify(data, case, k):
	distance_queue = []
	# compara atributos do novo caso com toda a base de dados
	for j in range(len(data)):
		distance = 0
		if case[0] != int(data[j][1]):
			distance += 1
		if case[0] != int(data[j][2]):
			distance += 1
		if case[0] != int(data[j][3]):
			distance += 1
		if case[0] != int(data[j][4]):
			distance += 1
		heapq.heappush(distance_queue, (distance, j))
	
	# encontra classe predominante nos k vizinhos mais próximos
	counter = [0]*3
	for i in range(k):
		shorter_distance, neighbor = heapq.heappop(distance_queue)
		counter[int(data[neighbor][5])-1] += 1
	
	predicted_class = 0
	matches = 0
	for m in range(len(counter)):
		if counter[m] > matches:
			predicted_class = m+1
			matches = counter[m]
	print("\nClasse", predicted_class)
	return

def k_Fold_Cross_Validation(data, partitions, neighbors):
	# divide data em x partições, sorteando uma para teste, e o resto para treino
	instances = []
	instances.extend(range(0, len(data)))
	random.shuffle(instances)

	hit = 0
	begin = 0
	end = (begin + len(data)//partitions) + 1
	for i in range(0, len(instances)):
		distance_queue = []
		if i != 0 and i%partitions == 0:
			begin = end
			end = (begin + len(data)//partitions) + 1
		for j in range(0, len(instances)):
			if not (j >= begin and j < end):
				# calcula distância para cada elemento e os insere numa fila de prioridade por menor distância
				distance = 0
				if int(data[instances[i]][1]) != int(data[instances[j]][1]):
					distance += 1
				if int(data[instances[i]][2]) != int(data[instances[j]][2]):
					distance += 1
				if int(data[instances[i]][3]) != int(data[instances[j]][3]):
					distance += 1
				if int(data[instances[i]][4]) != int(data[instances[j]][4]):
					distance += 1
				heapq.heappush(distance_queue, (distance, instances[j]))
		# pega os k vizinhos mais próximos e conta sua classes
		counter = [0]*3
		for k in range(neighbors):
			shorter_distance, neighbor = heapq.heappop(distance_queue)
			counter[int(data[neighbor][5])-1] += 1
		
		# escolhe a classe presente em maior quantidade
		predicted_class = 0
		matches = 0
		for m in range(len(counter)):
			if counter[m] > matches:
				predicted_class = m+1
				matches = counter[m]
		
		# comparar classe escolhida e classe real de cada instância para definir acurácia
		if predicted_class == int(data[i][5]):
			hit += 1
	accuracy = round((hit/len(instances)), 2)
	return accuracy

def normalize(data):
	maximum = [-1]*(len(data[0])-1)
	minimum = [float('inf')]*(len(data[0])-1)
	for i in range(len(data)):
		if float(data[i][0]) < minimum[0]:
			minimum[0] = float(data[i][0])
		if float(data[i][0]) > maximum[0]:
			maximum[0] = float(data[i][0])
		
		if float(data[i][1]) < minimum[1]:
			minimum[1] = float(data[i][1])
		if float(data[i][1]) > maximum[1]:
			maximum[1] = float(data[i][1])
		
		if float(data[i][2]) < minimum[2]:
			minimum[2] = float(data[i][2])
		if float(data[i][2]) > maximum[2]:
			maximum[2] = float(data[i][2])
		
		if float(data[i][3]) < minimum[3]:
			minimum[3] = float(data[i][3])
		if float(data[i][3]) > maximum[3]:
			maximum[3] = float(data[i][3])
	
	for j in range(len(data)):
		data[j][0] = ((float(data[j][0]) - minimum[0])/(maximum[0] - minimum[0]))
		data[j][1] = ((float(data[j][1]) - minimum[1])/(maximum[1] - minimum[1]))
		data[j][2] = ((float(data[j][2]) - minimum[2])/(maximum[2] - minimum[2]))
		data[j][3] = ((float(data[j][3]) - minimum[3])/(maximum[3] - minimum[3]))
	return data

def k_Fold_Cross_Validation_v2(data, partitions, neighbors):
	# divide data em x partições, sorteando uma para teste, e o resto para treino
	instances = []
	instances.extend(range(0, len(data)))
	random.shuffle(instances)

	hit = 0
	begin = 0
	end = (begin + len(data)//partitions) + 1
	for i in range(0, len(instances)):
		distance_queue = []
		if i != 0 and i%partitions == 0:
			begin = end
			end = (begin + len(data)//partitions) + 1
		for j in range(0, len(instances)):
			if not (j >= begin and j < end):
				# calcula distância para cada elemento e os insere numa fila de prioridade por menor distância
				distance = 0
				distance += (float(data[instances[i]][0]) - float(data[instances[j]][0]))**2
				distance += (float(data[instances[i]][1]) - float(data[instances[j]][1]))**2
				distance += (float(data[instances[i]][2]) - float(data[instances[j]][2]))**2
				distance += (float(data[instances[i]][3]) - float(data[instances[j]][3]))**2
				distance = math.sqrt(distance)
				heapq.heappush(distance_queue, (distance, instances[j]))
		
		# pega os k vizinhos mais próximos e conta sua classes
		counter = [0]*3
		for k in range(neighbors):
			shorter_distance, neighbor = heapq.heappop(distance_queue)
			if data[neighbor][4] == 'Iris-setosa\n':
				counter[0] += 1
			if data[neighbor][4] == 'Iris-versicolor\n':
				counter[1] += 1
			if data[neighbor][4] == 'Iris-virginica\n':
				counter[2] += 1

		# escolhe a classe presente em maior quantidade
		predicted_class = 0
		matches = 0
		for m in range(len(counter)):
			if counter[m] > matches:
				predicted_class = m+1
				matches = counter[m]
		
		# comparar classe escolhida e classe real de cada instância para definir acurácia
		if predicted_class == 1:
			predicted_class = 'Iris-setosa\n'
		if predicted_class == 2:
			predicted_class = 'Iris-versicolor\n'
		if predicted_class == 3:
			predicted_class = 'Iris-virginica\n'
		
		if predicted_class == data[i][4]:
			hit += 1
	accuracy = round((hit/len(instances)), 2)
	return accuracy

def classify_v2(data, case, k):
	distance_queue = []
	# calcula distância entre o novo caso e toda a base de dados
	for j in range(len(data)):
		distance = 0
		distance += (case[0] - float(data[j][0]))**2
		distance += (case[1] - float(data[j][1]))**2
		distance += (case[2] - float(data[j][2]))**2
		distance += (case[3] - float(data[j][3]))**2
		distance = math.sqrt(distance)
		heapq.heappush(distance_queue, (distance, j))
	
	# encontra classe predominante nos k vizinhos mais próximos
	counter = [0]*3
	for i in range(k):
		shorter_distance, neighbor = heapq.heappop(distance_queue)
		if data[neighbor][4] == 'Iris-setosa\n':
			counter[0] += 1
		if data[neighbor][4] == 'Iris-versicolor\n':
			counter[1] += 1
		if data[neighbor][4] == 'Iris-virginica\n':
			counter[2] += 1
	
	predicted_class = 0
	matches = 0
	for m in range(len(counter)):
		if counter[m] > matches:
			predicted_class = m+1
			matches = counter[m]
	if predicted_class == 1:
		predicted_class = 'Iris-setosa\n'
	if predicted_class == 2:
		predicted_class = 'Iris-versicolor\n'
	if predicted_class == 3:
		predicted_class = 'Iris-virginica\n'
	print("\nClasse", predicted_class)
	return

# MAIN
print("Iniciando algoritmo classificador k-NN...")
database = int(input("\nQue base de dados deseja utilizar : (1) lenses, (2) iris : "))
if database == 1:
	with open("lenses.data.txt") as textFile:
		data = [line.split() for line in textFile]
	print("\nNúmero de atributos:", len(data[0])-2)
	print("Número de instâncias:", len(data))

	# o limite superior de k é definido como a raiz quadrada da quantidade de instâncias
	top_limit = round(math.sqrt(len(data)))
	
	# usa cálculo de acurácia para definir o melhor k a ser usado dentro do limite
	print("\nUsando k-Fold Cross Validation para escolher valor adequado de k para consulta...\n")
	accuracy_queue = []
	for i in range(top_limit):
		print("Avaliando algoritmo para k =", i+1)
		accuracy = k_Fold_Cross_Validation(data, top_limit, i+1)
		heapq.heappush(accuracy_queue, ((-1)*accuracy, i+1))
		print("Acurácia calculada:", round(accuracy*100), "%\n")

	# escolhe k com maior acurácia
	accuracy = heapq.heappop(accuracy_queue)
	print("Usando k =", accuracy[1], "com acurácia de", accuracy[0]*(-1))

	print("\nAlgoritmo pronto para classificação, insira um caso abaixo:")
	choice = 1
	while choice == 1:
		new_case = [0]*4
		new_case[0] = int(input("\nAge of the patient: (1) young, (2) pre-presbyopic, (3) presbyopic : "))
		new_case[1] = int(input("Spectacle prescription: (1) myope, (2) hypermetrope : "))
		new_case[2] = int(input("Astigmatic: (1) no, (2) yes : "))
		new_case[3] = int(input("Tear production rate: (1) reduced, (2) normal : "))

		classify(data, new_case, accuracy[1])
		choice = int(input("\nDeseja fazer nova consulta ? (1) sim, (2) não : "))
else:
	with open("iris.data.txt") as textFile:
		data = [line.split(",") for line in textFile]
	print("\nNúmero de atributos:", len(data[0])-1)
	print("Número de instâncias:", len(data))

	top_limit = round(math.sqrt(len(data)))

	# normaliza os dados
	data = normalize(data)

	print("\nUsando k-Fold Cross Validation para escolher valor adequado de k para consulta...\n")
	accuracy_queue = []
	for i in range(top_limit):
		print("Avaliando algoritmo para k =", i+1)
		accuracy = k_Fold_Cross_Validation_v2(data, top_limit, i+1)
		heapq.heappush(accuracy_queue, ((-1)*accuracy, i+1))
		print("Acurácia calculada:", round(accuracy*100), "%\n")
	
	accuracy = heapq.heappop(accuracy_queue)
	print("Usando k =", accuracy[1], "com acurácia de", accuracy[0]*(-1))

	print("\nAlgoritmo pronto para classificação, insira um caso abaixo:")
	choice = 1
	while choice == 1:
		new_case = [0]*4
		new_case[0] = float(input("\nSepal length (in cm): "))
		new_case[1] = float(input("Sepal width (in cm): "))
		new_case[2] = float(input("Petal length (in cm): "))
		new_case[3] = float(input("Petal width (in cm): "))

		classify_v2(data, new_case, accuracy[1])
		choice = int(input("Deseja fazer nova consulta ? (1) sim, (2) não : "))