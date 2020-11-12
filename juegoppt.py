#PIEDRA PAPEL O TIJERAS

from random import choice

def seleccion_usuario():
	usuario = input('\npiedra, papel o tijera: ')

	return usuario.lower()

def comparacion(usuario, pc, cont_usuario, cont_pc):
	if usuario == 'piedra':
		if pc == 'tijera':
			resultado = 'Ganaste!!! =D'
			cont_usuario += 1
		elif pc == 'papel':
			resultado = 'Perdiste... =('
			cont_pc += 1
	elif usuario == 'tijera':
		if pc == 'papel':
			resultado = 'Ganaste!!! =D'
			cont_usuario += 1
		elif pc == 'piedra':
			resultado = 'Perdiste... =('
			cont_pc += 1
	else:
		if pc == 'piedra':
			resultado = 'Ganaste!!! =D'
			cont_usuario += 1
		elif pc == 'tijera':
			resultado = 'Perdiste... =('
			cont_pc += 1

	return(resultado, cont_usuario, cont_pc)

print('Juguemos hasta en 5 oportunidades, \nquien gane 3 rondas gana el juego')
opciones = ['piedra', 'papel', 'tijera']
cont = 1
cont_usuario = 0
cont_pc = 0

for cont in range(1, 6):

	usuario = seleccion_usuario()

	pc = choice(opciones)

	if usuario in opciones:
		if usuario == pc:
			print('Esto es un empate.')
		else:
			resultado, cont_usuario, cont_pc = comparacion(usuario, pc, cont_usuario, cont_pc)
			print(resultado,'por que saque',pc)

		if cont_usuario == 3:
			mensaje = print('\n\nGanaste',str(cont_usuario),'a',str(cont_pc))
			break
		elif cont_pc == 3:
			mensaje = print('\n\nPerdiste',str(cont_usuario),'a',str(cont_pc))
			break

		if cont == 4:
			print('\nViene la ultima')
		elif cont == 5 and cont_usuario < 3 and cont_pc < 3:
			mensaje = print('\nEsto quedo:\nTU',str(cont_usuario),'\nPC',str(cont_pc))
	else:
		print('Por favor ingrese una opcion valida')