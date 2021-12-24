#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CRUD.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  
#  

import pandas as pd

def split_dataframe_by_row(row, items):
	# Carga pandas y lee el archivo preguntas.csv, separando las preguntas
	# en categorias en distintos data frames.
	df = pd.read_csv('Preguntas.csv',header = 0)
	return [df[df[row] == item] for item in items]

def save_ranking(player, score):
	# Funcion que guarda el puntaje del jugador
	ranking = pd.read_csv('score.csv', header = 0)
	ranking.loc[len(ranking.index)] = [player, score]
	print(' Ranking '.center(50, '='))
	ranking = ranking.sort_values(by = 'Score', ascending = 0)
	print(ranking)
	ranking.to_csv('score.csv', index = False)

def save_question(question, correct, wrong1, wrong2, wrong3, category, level):
	# Funcion que guarda la pregunta configurada
	questions = pd.read_csv('Preguntas.csv', header = 0)
	questions.loc[len(questions.index)] = [question, correct, wrong1, wrong2, wrong3, category, level]
	print(' Preguntas '.center(50, '='))
	questions = questions.sort_values(by = 'Categoria', ascending = 0)
	print(questions)
	questions.to_csv('Preguntas.csv', index = False)

def main(args):
	
	player = input('Ingrese su nombre: ')
	score = int(input('Ingrese un numero: '))
	
	if score > 0:
		save_ranking(player, score)
	
	timeout = 10
	t = Timer(timeout, print, ['Sorry, times up'])
	t.start()
	prompt = "You have %d seconds to choose the correct answer...\n" % timeout
	answer = input(prompt)
	t.cancel()

	return 0

if __name__ == '__main__':
	import sys
	from threading import Timer
	sys.exit(main(sys.argv))
