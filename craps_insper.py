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

	informar_inicio()				# dá informações gerais sobre o funcionamento do jogo
	cumprimentar(fichas)			# STICKMAN cumprimenta o jogador
	input('STICKMAN:\tVamos lá!\n')	# fala do STICKMAN

	while fichas > 0:	# ciclo principal do jogo

		informar_rodada(fichas)	# informa a quantidade de fichas e a fase atual do jogo

		quer_apostar = perguntar_bool('E aí, vai APOSTAR ou SAIR?', entradas_possiveis['apostar'], entradas_possiveis['sair'])	# pergunta se quer apostar ou sair do jogo, guarda o valor Booleano em 'quer_apostar'

		if not quer_apostar: break	# se não quiser apostar, ou seja, quiser sair, quebra o loop

		apostas = {}	# dicionário para guardar os tipos de apostas ativas e os respectivos valores

		while quer_apostar:	# loop de apostas do COME OUT

			aposta = perguntar_string('Você pode fazer uma PASS LINE BET, uma FIELD BET, uma ANY CRAPS BET ou uma TWELVE BET.', apostas_come_out).upper()	# diz que apostas podem ser feitas, e pergunta qual quer ser feita
			quantidade = perguntar_numero('Quanto quer apostar?', 1, fichas - sum(apostas.values()))	# pergunta quanto quer apostar na aposta especifica, e impede de apostar mais do que tem

			apostas = registrar_aposta(aposta, quantidade, apostas)	# registra a aposta no dicionário de apostas

			if fichas == sum(apostas.values()):	# se a quantidade apostada for igual as fichas do jogador, quebra o loop de apostas
				print('STICKMAN:\tVocê não tem fichas o suficiente para fazer novas apostas!')
				break

			if not perguntar_bool('Quer fazer outra aposta? SIM ou NÃO.', entradas_possiveis['positivo'], entradas_possiveis['negativo']): break	# pergunta se o jogador quer apostar mais, se quiser, continua o loop

		informar_pre_lancamento(fichas, apostas)	# informa a quantidade de fichas, as apostas feitas e a fase atual
		
		input('\n\tPRESSIONE ENTER PARA ROLAR OS DADOS')

		dados = [randint(1,6), randint(1,6)]	# lançamento dos dados
		resultado = sum(dados)
		input('\n\tRESULTADOS: %d + %d = %d' % (dados[0], dados[1], resultado))	# imprime o resultado dos lançamentos
		
		apostas, fichas, point = resultado_apostas_come_out(apostas, resultado, fichas)	# analisa o resultado das apostas, atualiza o dicionário de apostas, qtde. de fichas e se vai pra fase point ou não

		input('\n\tPRESSIONE ENTER PARA CONTINUAR')

		print()

		numero_point = resultado 	# fixa o número point

		while point and fichas > 0:	# loop da fase de point

			informar_rodada(fichas, False, numero_point)	# informa o número de fichas, a fase, e o número  Point

			if fichas - sum(apostas.values()) == 0:			# impede apostar fichas já apostadas
				input('STICKMAN:\tVocê não tem fichas o suficiente para fazer novas apostas!')
				quer_apostar = False

			else:	# caso tenha fichas disponíveis, pergunta se quer apostar mais ou não
				quer_apostar = perguntar_bool('E aí, vai apostar, SIM ou NÃO?', entradas_possiveis['positivo'], entradas_possiveis['negativo'])

			while quer_apostar:	# loop de apostas da fase Point

				aposta = perguntar_string('Você pode fazer uma FIELD BET, uma ANY CRAPS BET ou uma TWELVE BET.', apostas_point).upper()	# diz que apostas podem ser feitas, e pergunta qual quer ser feita
				quantidade = perguntar_numero('Quanto quer apostar?', 1, fichas - sum(apostas.values()))	# pergunta quanto quer apostar na aposta especifica, e impede de apostar mais do que tem

				apostas = registrar_aposta(aposta, quantidade, apostas)	# registra a aposta no dicionário de apostas

				if fichas == sum(apostas.values()):	# se a quantidade apostada for igual as fichas do jogador, quebra o loop de apostas
					print('STICKMAN:\tVocê não tem mais fichas para apostar!')
					break

				if not perguntar_bool('Quer fazer outra aposta, SIM ou NÃO?', entradas_possiveis['positivo'], entradas_possiveis['negativo']): break	# pergunta se quer fazer uma nova aposta, quebra o loop caso não queira

			informar_pre_lancamento(fichas, apostas, False, numero_point)	# informa a quantidade de fichas, as apostas feitas e a fase atual
			
			input('\n\tPRESSIONE ENTER PARA ROLAR OS DADOS')

			dados = [randint(1,6), randint(1,6)]	# faz lançamento dos dados
			resultado = sum(dados)
			input('\n\tRESULTADOS: %d + %d = %d' % (dados[0], dados[1], resultado))	# imprime o resultado dos lançamentos

			apostas, fichas, point = resultado_apostas_point(apostas, resultado, numero_point, fichas)	# analisa o resultado das apostas, atualiza o dicionário de apostas, qtde. de fichas e se volta pra fase come out ou não

			input('\n\tPRESSIONE ENTER PARA CONTINUAR')

	# falas de fim de jogo
	if fichas > fichas_gratis:
		print('\nSTICKMAN:\tMandou bem! Bom jogo.\n')
	elif fichas == fichas_gratis:
		print('\nSTICKMAN:\tPoxa, não ganhou nem perdeu! Bom jogo!\n')
	elif fichas == 0:
		print('\nSTICKMAN:\tPuts, você ficou sem fichas! Bom jogo!\n')


def informar_inicio():
	''' dá informações gerais sobre o funcionamento do jogo ao jogador '''

	print('\n --- --- --- INFORMAÇÕES  GERAIS --- --- ---')
	input('  - A tecla ENTER serve para passar para a próxima fala;')
	input('  - As perguntas do STICKMAN devem ser respondidas com entradas exatas.')
	print(' --- --- --- --- --- --- --- --- --- --- ---\n')

	input('APERTE ENTER PARA COMEÇAR')
	print()

def informar_rodada(fichas, come_out = True, numero_point = 0):
	''' informa a quantidade de fichas e a fase atual '''

	if come_out: print('\tFASE: COME OUT')
	else: print('\tFASE: POINT no %d' % numero_point)
	print('\tFICHAS: %d\n' % fichas)

def informar_pre_lancamento(fichas, apostas, come_out = True, numero_point = 0):
	''' informa a quantidade de fichas, apostas ativas e fase atual '''

	if come_out: print('\n\tFASE: COME OUT')
	else: print('\n\tFASE: POINT no %d' % numero_point)
	print('\tFICHAS: %d' % fichas)
	print('\tAPOSTAS:')

	for aposta in apostas.keys():

		if come_out:
			print('\t- %s: %d' % (aposta, apostas[aposta]))

		else:
			print('\t- %s: %d' % (aposta, apostas[aposta]), end = '')
			if aposta == entradas_possiveis['pass line']:print(' no %d' % numero_point)
			else: print()

def registrar_aposta(aposta, quantidade, apostas):
	''' registra novas apostas no dicionário de apostas '''

	try:
		if aposta in apostas.keys(): apostas[aposta] += quantidade
		elif quantidade != 0: apostas[aposta] = quantidade
	except: pass

	return apostas

def resultado_apostas_point(apostas, resultado, numero_point, fichas):
	''' analisa e apresenta o resultado das apostas, atualiza o dicionário de apostas, o número de fichas e a fase do jogo '''

	point = True

	for aposta in apostas.keys():
		print('\t- %s:' % aposta, end = ' ')

		del_passline = False

		if aposta.lower() == entradas_possiveis['pass line']:

			if resultado == numero_point:
				print('GANHOU %d' % apostas[aposta])
				fichas += apostas[aposta]
				del_passline = True
				point = False

			elif resultado == 7:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]
				del_passline = True
				point = False

			else:
				print('%d no %d' % (apostas[aposta], numero_point))

		elif aposta.lower() == entradas_possiveis['field']:

			if resultado == 2:
				print('GANHOU %d' % (apostas[aposta] * 2))
				fichas += apostas[aposta] * 2

			elif resultado == 12:
				print('GANHOU %d' % (apostas[aposta] * 3))
				fichas += apostas[aposta] * 3

			elif resultado in [3, 4, 9, 10, 11]:
				print('GANHOU %d' % apostas[aposta])
				fichas += apostas[aposta]

			else:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]

		elif aposta.lower() == entradas_possiveis['any craps']:

			if resultado in [2, 3, 12]:
				print('GANHOU %d' % (apostas[aposta] * 7))
				fichas += apostas[aposta] * 7

			else:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]

		elif aposta.lower() == entradas_possiveis['twelve']:

			if resultado == 12:
				print('GANHOU %d' % (apostas[aposta] * 30))
				fichas += apostas[aposta] * 30

			else:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]

	if del_passline: del apostas[entradas_possiveis['pass line'].upper()]
	try: del apostas[entradas_possiveis['any craps'].upper()]
	except: pass
	try: del apostas[entradas_possiveis['twelve'].upper()]
	except: pass
	try: del apostas[entradas_possiveis['field'].upper()]
	except: pass

	return apostas, fichas, point

def resultado_apostas_come_out(apostas, resultado, fichas):
	''' analisa e apresenta o resultado das apostas, atualiza o dicionário de apostas, o número de fichas e a fase do jogo '''

	point = False 				# assume que não vai para a fase de point

	if resultado in [4, 5, 6, 8, 9, 10]:	# se o resultado estiver dentro desses números, passar para fase Point
		point = True

	for aposta in apostas.keys():
		print('\t- %s:' % aposta, end = ' ')

		del_passline = False

		if aposta.lower() == entradas_possiveis['pass line']:

			if point:
				print('%d no %d' % (apostas[aposta], resultado))

			elif resultado in [7, 11]:
				print('GANHOU %d' % apostas[aposta])
				fichas += apostas[aposta]
				del_passline = True

			else:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]
				del_passline = True
		elif aposta.lower() == entradas_possiveis['field']:

			if resultado == 2:
				print('GANHOU %d' % (apostas[aposta] * 2))
				fichas += apostas[aposta] * 2

			elif resultado == 12:
				print('GANHOU %d' % (apostas[aposta] * 3))
				fichas += apostas[aposta] * 3

			elif resultado in [3, 4, 9, 10, 11]:
				print('GANHOU %d' % apostas[aposta])
				fichas += apostas[aposta]

			else:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]

		elif aposta.lower() == entradas_possiveis['any craps']:

			if resultado in [2, 3, 12]:
				print('GANHOU %d' % (apostas[aposta] * 7))
				fichas += apostas[aposta] * 7

			else:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]

		elif aposta.lower() == entradas_possiveis['twelve']:

			if resultado == 12:
				print('GANHOU %d' % (apostas[aposta] * 30))
				fichas += apostas[aposta] * 30

			else:
				print('PERDEU %d' % apostas[aposta])
				fichas -= apostas[aposta]

	if del_passline: del apostas[entradas_possiveis['pass line'].upper()]
	try: del apostas[entradas_possiveis['any craps'].upper()]
	except: pass
	try: del apostas[entradas_possiveis['twelve'].upper()]
	except: pass
	try: del apostas[entradas_possiveis['field'].upper()]
	except: pass

	return apostas, fichas, point

def cumprimentar(fichas_gratis):
	''' cumprimenta o jogador e lhe dá fichas grátis '''

	input('STICKMAN:\tBem-vindo ao Craps Insper!')
	input('STICKMAN:\tVocê dispõe de %d fichas por conta da casa.' % fichas_gratis)
	input('STICKMAN:\tSuponho que você saiba as regras do jogo. Caso não saiba, não vale reclamar.')

def questionar_resposta():
	''' fala padrão para entradas irreconhecíveis '''

	input('STICKMAN:\tNão entendi o que você disse, companheiro!')

def perguntar_string(pergunta, respostas_esperadas):
	''' pergunta que exige como resposta uma string; valida a resposta obtida e pergunta de novo caso seja uma resposta irreconhecível '''

	while True:

		print('STICKMAN:\t' + pergunta)
		resposta = input('JOGADOR:\t').lower()

		if resposta not in respostas_esperadas:
			questionar_resposta()

		else: return resposta

def perguntar_numero(pergunta, minimo, maximo):
	''' pergunta que exige como resposta um inteiro; valida a resposta obtida e pergunta de novo caso seja uma resposta irreconhecível '''

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
	''' pergunta que exige como resposta uma string e a traduz em true ou false; valida a resposta obtida e pergunta de novo caso seja uma resposta irreconhecível '''

	while True:

		print('STICKMAN:\t' + pergunta)
		resposta = input('JOGADOR:\t').lower()

		if resposta == resposta_true: return True
		if resposta == resposta_false: return False
		else: questionar_resposta()

iniciar(1000)	# inicia o jogo com 1000 fichas grátis





