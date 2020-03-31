from random import randint

entradas_possiveis = {
	'positivo': 'Sim',
	'negativo': 'Não',
	'sair': 'Sair',
	'apostar': 'Apostar',
	'pass line bet': 'Pass Line Bet',
	'field': 'Field',
	'any craps': 'Any Craps',
	'twelve': 'Twelve'
	}

def iniciar(fichas_gratis):
	''' inicia o programa '''

	fichas = fichas_gratis

	informar()
	cumprimentar(fichas)
	input('STICKMAN:\tVamos lá!')

	rodadas = 0

	while fichas > 0:

		print('\tFASE: COME OUT')
		print('\tFICHAS: %d' % fichas)
		print('STICKMAN:\tE aí, vai apostar ou sair?')
		resposta = input('JOGADOR:\t')

		if resposta == entradas_possiveis['sair']: break

		resultado = randint(1,6) + randint(1,6)
		print(resultado)
		fichas -= 1

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
	input('STICKMAN:\tVocê dispõe de %d fichas por conta da casa' % fichas_gratis)
	input('STICKMAN:\tSuponho que você saiba as regras do jogo. Caso não saiba, não vale reclamar.')

iniciar(1000)





