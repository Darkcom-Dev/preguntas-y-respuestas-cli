#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  questions.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  

import random

class Question:
	def __init__(self, question, answers, category, level):
		self.__question = question
		self.__answers = answers
		self.__category = category
		self.__level = level
	'''
	def __del__(self):
		# Funcion especial que hereda de la clase Object
		print(f'Pregunta eliminada: {self.__question}')
	'''
	def __str__(self):
		# Funcion especial que sobreescribe la informacion acerca de la clase.
		# Metodo heredado de object
		return (f'Pregunta: {self.__question}, Categoria: {self.__category}, Nivel: {self.__level}')

	#===========================|
	# Getters					|
	#===========================|
	@property
	def question(self):
		return self.__question
		
		
	@property
	def answers(self):
		return self.__answers
		
	@property
	def category(self):
		return self.__category
		
	@property
	def level(self):
		return self.__level
	'''
	#===========================|
	# Setters					|
	#===========================|
	@question.setter
	def question(self, question):
		self.__question = question
		
	@answers.setter
	def answers(self, answers):
		self.__answers = answers
	
	def __del__(self):
		# Funcion especial que hereda de la clase Object
		print(f'Eliminada la pregunta: {self.__question}')

	def __str__(self):
		# Funcion especial que sobreescribe la informacion acerca de la clase.
		# Metodo heredado de object
		return (f'Pregunta: {self.__question}, Categoria: {self.__category}, Nivel: {self.__level}')
	'''
	#===========================|
	# Funciones de Clase		|
	#===========================|



	def show(self):
		# Muestra la pregunta como se verá en el concurso
		rand = self.__answers.copy()
		correct = self.__answers[0]
		random.shuffle(rand)
		print(f' {self.__category} '.center(50,'='))
		text = f'''
Pregunta: {self.__question}
1.	{rand[0]}
2.	{rand[1]}
3.	{rand[2]}
4.	{rand[3]}
		'''
		print(text)
		index = rand.index(correct)
		# print(index + 1) # Descomente la linea para saber el resultado
		return index + 1

def main(args):
	
	test = Question('De que color es el caballo blanco de Bolivar', ['Blanco','Rojo', 'Verde', 'Azul'], 'Historia',1)
	print(test)
	result = test.show()
	
	
	return 0

if __name__ == '__main__':
	import sys
	
	sys.exit(main(sys.argv))
