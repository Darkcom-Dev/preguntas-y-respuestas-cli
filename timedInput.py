#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CancelInput.py
#  
#  Copyright 2021 Braulio Madrid <darkcom@darkcom-X455LD>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import select

class TimeoutExpired(Exception):
	pass


def input_with_timeout(prompt, timeout):
	# Contador de tiempo para retornar una respuesta
	sys.stdout.write(prompt)
	sys.stdout.flush()
	ready, _, _ = select.select([sys.stdin], [],[], timeout)
	if ready:
		return sys.stdin.readline().rstrip('\n') # expect stdin to be line-buffered
	raise TimeoutExpired

def timed_input(prompt, timeout, failed_prompt, failed = None):
	# Devuelve una respuesta por defecto si se agota el tiempo
	try:
		return input_with_timeout(prompt, timeout)
	except TimeoutExpired:
		print(failed_prompt)
		return failed

def secure_int_input(prompt, default):
	# Devuelve un número entero garantizado
	try:
		return int(input(prompt))
	except ValueError:
		option = default
		
def secure_string_input(prompt, default = None):
	while True:
		input_return = input(prompt)
		if input_return != '':
			return input_return
		else:
			if default != None:
				return default

def main(args):
	
	prompt = 'Escribe un numero del 1 al 4 para responder o 0 para retirarse: '
	get = int(timed_input(prompt, 10, 'Lo siento, acabó el tiempo', 0))
	print(f'type: {type(get)}, answer: {get}')
	
	return 0

if __name__ == '__main__':

	#from threading import Timer
	sys.exit(main(sys.argv))
