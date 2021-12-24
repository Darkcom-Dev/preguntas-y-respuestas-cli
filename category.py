#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  category.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  


import random

class Category:
	def __init__(self, name, questions):
		self.__name = name
		self.__questions = questions
	'''
	def __del__(self):
		# Funcion especial que hereda de la clase Object
		print(f'fue eliminado la categoria: {self.__name}')
	'''
	def __str__(self):
		# Funcion especial que sobreescribe la informacion acerca de la clase.
		# Metodo heredado de object
		return (f'Categoria: {self.__name}, Questions: {len(self.__questions)}')
		
	#===========================|
	# Getters					|
	#===========================|
	@property
	def name(self):
		return self.__name
		
	@property
	def questions(self):
		return self.__questions
	'''
	#===========================|
	# Setters					|
	#===========================|
	@name.setter
	def name(self, name):
		self.__name = name
		
	@questions.setter
	def questions(self, questions):
		self.__questions = questions
	'''
	#===========================|
	# Funciones de clase		|
	#===========================|
	def select(self):
		print(self.__name)
		result = self.__questions.copy()
		# random.shuffle(result) # TODO: Revolver preguntas del mismo nivel
		return result


def main(args):
	return 0

if __name__ == '__main__':
	import sys
	
	sys.exit(main(sys.argv))
