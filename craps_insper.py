from random import randint

entradas_possiveis = {
	'positivo': 'sim',
	'negativo': 'não',
	'sair': 'sair',
	'apostar': 'apostar',
	'pass line': 'pass line bet',
	'field': 'field bet',
	'any craps': 'any craps bet',
	'twelve': 'twelve bet'
	}
apostas_come_out = [
	entradas_possiveis['pass line'],
	entradas_possiveis['field'],
	entradas_possiveis['any craps'],
	entradas_possiveis['twelve']
	]
apostas_point = [
	entradas_possiveis['field'],
	entradas_possiveis['any craps'],
	entradas_possiveis['twelve']
	]

def iniciar(fichas_gratis):
	''' inicia o programa '''

	fichas = fichas_gratis

	informar()
	cumprimentar(fichas)
	input('STICKMAN:\tVamos lá!\n')

	rodadas = 0

	while fichas > 0:

		print('\tFASE: COME OUT')
		print('\tFICHAS: %d\n' % fichas)

		apostar = perguntar_bool('E aí, vai APOSTAR ou SAIR?', entradas_possiveis['apostar'], entradas_possiveis['sair'])

		if not apostar: break

		apostas = {}

		while apostar:

			aposta = perguntar_string('Você pode fazer uma PASS LINE BET, uma FIELD BET, uma ANY CRAPS BET ou uma TWELVE BET.', apostas_come_out).upper()
			quantidade = perguntar_numero('Quanto quer apostar?', 1, fichas - sum(apostas.values()))

			try:
				if aposta in apostas.keys(): apostas[aposta] += quantidade
				else: apostas[aposta] = int(quantidade)
			except: pass

			if fichas == sum(apostas.values()):
				print('Você não tem mais fichas para apostar!')
				break

			if not perguntar_bool('Quer fazer outra aposta, SIM ou NÃO?', entradas_possiveis['positivo'], entradas_possiveis['negativo']): break

		print('\n\tFASE: COME OUT')
		print('\tAPOSTAS:')

		for aposta in apostas.keys():
			print('\t- %s: %d' % (aposta, apostas[aposta]))
		
		input('\n\tPRESSIONE ENTER PARA ROLAR DADOS')

		dados = [randint(1,6), randint(1,6)]
		resultado = sum(dados)
		input('\tRESULTADOS: %d + %d = %d' % (dados[0], dados[1], resultado))

		point = False
		point_number = resultado

		if resultado in [4, 5, 6, 8, 9, 10]:
			point = True
		
		for aposta in apostas.keys():
			print('\t- %s:' % aposta, end = ' ')

			if aposta.lower() == entradas_possiveis['pass line']:

				if point:
					print('POINT %d' % resultado)

				elif resultado in [7, 11]:
					print('GANHOU %d' % apostas[aposta])
					fichas += apostas[aposta]

				else:
					print('PERDEU %d' % apostas[aposta])
					fichas -= apostas[aposta]
			elif aposta.lower() == entradas_possiveis['field']:

				if resultado == 2:
					print('GANHOU %d' % apostas[aposta] * 2)
					fichas += apostas[aposta] * 2

				elif resultado == 12:
					print('GANHOU %d' % apostas[aposta] * 3)
					fichas += apostas[aposta] * 3

				elif resultado in [3, 4, 9, 10, 11]:
					print('GANHOU %d' % apostas[aposta])
					fichas += apostas[aposta]

				else:
					print('PERDEU %d' % apostas[aposta])
					fichas -= apostas[aposta]
			elif aposta.lower() == entradas_possiveis['any craps']:

				if resultado in [2, 3, 12]:
					print('GANHOU %d' % apostas[aposta] * 7)
					fichas += apostas[aposta] * 7

				else:
					print('PERDEU %d' % apostas[aposta])
					fichas -= apostas[aposta]
			elif aposta.lower() == entradas_possiveis['twelve']:

				if resultado == 12:
					print('GANHOU %d' % apostas[aposta] * 30)
					fichas += apostas[aposta] * 30

				else:
					print('PERDEU %d' % apostas[aposta])
					fichas -= apostas[aposta]

		print()

		while point:

			print('\tFASE: POINT no %d' % point_number)
			print('\tFICHAS: %d\n' % fichas)

			apostar = perguntar_bool('E aí, vai apostar, SIM ou NÃO?', entradas_possiveis['positivo'], entradas_possiveis['negativo'])

			while apostar:

				aposta = perguntar_string('Você pode fazer uma FIELD BET, uma ANY CRAPS BET ou uma TWELVE BET.', apostas_point).upper()
				quantidade = perguntar_numero('Quanto quer apostar?', 1, fichas - sum(apostas.values()))

				try:
					if aposta in apostas.keys(): apostas[aposta] += quantidade
					else: apostas[aposta] = int(quantidade)
				except: pass

				if fichas == sum(apostas.values()):
					print('Você não tem mais fichas para apostar!')
					break

				if not perguntar_bool('Quer fazer outra aposta, SIM ou NÃO?', entradas_possiveis['positivo'], entradas_possiveis['negativo']): break


		rodadas += 1


def informar():
	''' dá informações gerais ao jogador '''

	print('\n --- --- --- INFORMAÇÕES  GERAIS --- --- ---')
	input('  - A tecla ENTER serve para passar para a próxima fala;')
	input('  - As perguntas do STICKMAN devem ser respondidas com entradas exatas.')
	print(' --- --- --- --- --- --- --- --- --- --- ---\n')

	input('APERTE ENTER PARA COMEÇAR')
	print()

def cumprimentar(fichas_gratis):
	''' cumprimenta o jogador e lhe dá fichas grátis '''

	input('STICKMAN:\tBem-vindo ao Craps Insper!')
	input('STICKMAN:\tVocê dispõe de %d fichas por conta da casa.' % fichas_gratis)
	input('STICKMAN:\tSuponho que você saiba as regras do jogo. Caso não saiba, não vale reclamar.')

def questionar_resposta():

	print('STICKMAN:\tNão entendi o que você disse, companheiro!')

def perguntar_string(pergunta, respostas_esperadas):

	while True:

		print('STICKMAN:\t' + pergunta)
		resposta = input('JOGADOR:\t').lower()

		if resposta not in respostas_esperadas:
			questionar_resposta()

		else: return resposta

def perguntar_numero(pergunta, minimo, maximo):

	while True:

		print('STICKMAN:\t' + pergunta)
		resposta = input('JOGADOR:\t')

		try:
			resposta = int(resposta)
			if resposta < minimo - 1: print('STICKMAN:\tVocê terá que apostar mais que isso.')
			elif resposta < minimo:
				print('STICKMAN: \tOK, OK, ninguém é obrigado a apostar!')
				break
			elif resposta > maximo: print('STICKMAN:\tOpa, calma lá! Você só tem %d fichas para apostar.' % maximo)
			else: return resposta

		except: questionar_resposta()

def perguntar_bool(pergunta, resposta_true, resposta_false):

	while True:

		print('STICKMAN:\t' + pergunta)
		resposta = input('JOGADOR:\t').lower()

		if resposta == resposta_true: return True
		if resposta == resposta_false: return False
		else: questionar_resposta()

iniciar(1000)





