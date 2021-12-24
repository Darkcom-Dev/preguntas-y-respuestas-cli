#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Concurso de preguntas y respuestas.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
# []1 - Clase preguntas con 4 opciones de eleccion
# 2 - Pasar el nivel a la clase categoria
# []3 - Debe existir minimo 5 preguntas por categoria
# []4 - Debe existir 5 rondas
# []3 - Se debe extraer una pregunta por cada ronda de forma aleatoria
# []6 - Cada ronda otorga premios o puntos.
# []7 - El jugador puede retirarse en cualquier momento con el premio acumulado
# []8 - Si pierde al responder, se vá sin el acumulado

# 1. Precondiciones: Debe de tener 25 preguntas (5 preguntas por categorías) para 5 rondas, cada categoría tiene una complejidad o nivel de dificultad, cada ronda debe asignarle un premio que el jugador va a ganar, el premio puede ser puntos o dinero.
# []2. El jugador inicia con la primera ronda, el sistema busca la categoría del primer nivel y escoge una pregunta de esa categoría. 
# []3. El Jugador selecciona una opción de las 4 opciones que tiene, si pierde se finaliza el juego si gana continua a la siguiente ronda.
# []4. La siguiente ronda selecciona una pregunta de un grado de complejidad mayor según la categoría. Hace el mismo comportamiento del ítem 4.
# []5. Si llega a la ronda 5 y pasa, entonces gana el juego, el premio mayor debería estar en la última ronda.

# []Configurar Juego: Crear las preguntas y respuestas (con 3 opciones erradas y 1 valida) con sus categorías correspondientes (mínimo 25 preguntas).
# []Iniciar el juego: se debe iniciar el juego con la primera ronda y de forma aleatoria debe seleccionar una pregunta según la categoría más baja.
# []Responder a la pregunta: debes seleccionar una opción de 4 posibles.
# []Aumentar de nivel: al responder de forma correcta deberás aumentar de nivel y de esa manera otorgar premios según la ronda que este. Ordena primero tus categorías y de esa manera sabrás en qué ronda estás ubicado.
# []Acomular premio: cada vez que ganes debes tener un premio total que tienes como jugador.
# []Fin del juego voluntario o ganara ronda final: se finaliza el juego porque el jugador deci y el acomulado pasa a l jugador (guarda los datos del jugador)
# []Fin del juego forzado: el sistema finaliza el juego porque no selecciono una pregunta correcta. (guarda los datos del jugador)
# []Persistencia de datos: al finalizar el juego se debe guardar los datos del jugador como histórico del juego.

import question as qst
import category as cat
import CRUD as crd
import timedInput as tmi
import pandas as pd
import random

def dataframe_to_questions(data):
	question = data['Pregunta'].to_list()
	answer1 = data['Respuesta 1'].to_list()
	answer2 = data['Respuesta 2'].to_list()
	answer3 = data['Respuesta 3'].to_list()
	answer4 = data['Respuesta 4'].to_list()
	cate = data['Categoria'].to_list()
	level = data['Nivel'].to_list()
	
	return [qst.Question(question[i],[answer1[i],answer2[i],answer3[i],answer4[i]],cate[i],level[i]) for i in range(len(question))]


def sort_dataframe_by_row(row, dfs):
	
	# Ordena los dataframes por el valor de una columna
	
	questions = []
	# transforma dataframes en preguntas
	for df in dfs:
		df = df.sort_values(by = row)
		questions.append(dataframe_to_questions(df))
	return questions

def show_question_count(questions):
	# Funcion de Debug se puede descartar
	# Muestra el total de preguntas por categoria
	print(' [Preguntas por categoria] '.center(50,'='))
	
	for question in questions:
		print(f" {question[0].category}: {len(question)}")
		

def start_game():
	
	# Entrada principal del programa como en los lenguajes mas antiguos
	debug = False
	string_categories = ['Lógica', 'Historia', 'Cine', 'Literatura', 'Videojuegos']
	
	# Separa las preguntas por categorias
	category_dfs = crd.split_dataframe_by_row('Categoria', string_categories)
	# Ordena las preguntas de las categorias por nivel
	category_questions = sort_dataframe_by_row('Nivel', category_dfs)
	# Muestra el total de preguntas por categoria
	if debug: show_question_count(category_questions)
	# Introduce las preguntas dentro de una clase de categoria
	all_categories = [cat.Category(string_categories[i], category_questions[i]) for i in range(len(string_categories))]
	# Revuelve las categorias
	random.shuffle(all_categories)
	if debug: print(*all_categories[0].questions, sep = '\n')
	
	#==============================|
	# Inicio de la logica del juego|
	#==============================|
	
	player = input('\nCual es tu nombre: ')
	if player == '':
		player = 'Anómino'
	score = 0
	_round = 0
	end_game = False
	
	while _round < 5 and end_game == False:
		print(f' Ronda {_round + 1} '.center(50,'='))
		
		current_question = all_categories[_round].select()
		answer = current_question[_round].show()
		if debug: print(current_question[_round])
		
		player_answer = int(tmi.timed_input('Escribe un numero del 1 al 4 para responder o 0 para retirarse: ',10,'\nSe acabó el tiempo',9))
			
		if player_answer == answer:
			print('Y la respuesta es.....!!!')
			print('CORRECTAAA!!!')
			score += current_question[_round].level * 100
		elif player_answer == 0:
			print(':( El concursante se ha retirado !!!')
			end_game = True
		else:
			print('Y las respuesta es....!!!!')
			print('Lo siento, has perdido')
			score = 0
			end_game = True
		
		_round += 1
		
	print(f'{player} has ganado un total de: $ {score}')
	
	# Solo guarda el valores en el ranking si el puntaje es mayor a cero
	if score > 0:
		crd.save_ranking(player, score)
	
	return 0

def main(args):
	start_game()
	return 0

# Las siguientes lineas existen por cuestiones de compatibilidad con
# sistemas linux o si se ejecutan dentro de una maquina virtual como
# repl.it

if __name__ == '__main__':
	import sys
	
	sys.exit(main(sys.argv))
