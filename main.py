#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  

def create_question():
	
	while True:
		question = tmi.secure_string_input('Ingrese la pregunta: ')
		correct = tmi.secure_string_input('Ingrese la respuesta correcta: ')
		wrong1 = tmi.secure_string_input('Ingrese la 1ra respuesta erronea: ')
		wrong2 = tmi.secure_string_input('Ingrese la 2da respuesta erronea: ')
		wrong3 = tmi.secure_string_input('Ingrese la 3ra respuesta erronea: ')
		category = tmi.secure_string_input('Ingrese la categoria a la que pertenece la pregunta: ')
		level = tmi.secure_int_input('Ingrese el nivel de dificultad: ',1)
		
		resume = f'''
		===========================================
		Sus respuestas fueron:
		Pregunta: {question}
		Respuesta: {correct}
		Otras: {wrong1}, {wrong2}, {wrong3}
		Categoria: {category}, Nivel: {level}
		===========================================
		¿Son correctos los datos?
		'''
		print(resume)
		
		option_print = '''
		┏━━━━━━━━━━━━━━━┓
		┃ 1 - Aceptar	┃░
		┃ 0 - Cancelar	┃░
		┃ 3 - Coregir	┃░
		┗━━━━━━━━━━━━━━━┛░
		    ░░░░░░░░░░░░░░
		'''
		print(option_print)
		option = tmi.secure_int_input('Opción: ',3)
		
		if option == 1:
			crd.save_question(question, correct, wrong1, wrong2, wrong3, category, level)
			break
		elif option == 0:
			print('Pregunta cancelada')
			break
		else:
			print('Reinicio o Corrección de datos')
		print(f'Pregunta: {question}')
		print()
		
	

def main(args):
	title = '''
	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
	┃ ¿Quien quiere ser millonario?	┃░
	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛░
	    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
	
	'''
	print(title)
	while True:
		option = tmi.secure_int_input('Elija 1 para jugar partida, Elija 2 para configurar preguntas: ',9)
		
		if option == 1:
			game.start_game()
			break
		elif option == 2:
			create_question()
			break
		else:
			print('Opcion incorrecta: Elija 1 o 2')
	return 0

if __name__ == '__main__':
	import sys
	import game
	import CRUD as crd
	import timedInput as tmi
	sys.exit(main(sys.argv))
