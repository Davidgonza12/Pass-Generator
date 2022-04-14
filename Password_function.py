# Autor : Eliel Gonzalez
import random

#constantes
minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
num = "0123456789"
simb = "[]{}()*;,.-_$#&!\=%?¿><@"

# funciones

def generador_completo(long):
	all = minus + mayus + num + simb

	password = "".join(random.choices(all,k = long))

	return password

#-------- 1 check box ---------#

def generador_mayus(long):
	all = mayus

	password = "".join(random.choices(all,k = long))

	return password


def generador_minus(long):
	all = minus

	password = "".join(random.choices(all,k = long))

	return password

def generador_numeros(long):
	all = num

	password = "".join(random.choices(all,k = long))

	return password

def generador_simbolos(long):
	all = simb

	password = "".join(random.choices(all,k = long))

	return password

#--------  2 check box ---------#
def generador_mayus_minus(long):
	all = mayus + minus

	password = "".join(random.choices(all,k = long))

	return password

def generador_mayus_num(long):
	all = mayus + num

	password = "".join(random.choices(all,k = long))

	return password



def generador_mayus_simb(long):
	all = mayus + simb

	password = "".join(random.choices(all,k = long))

	return password

def generador_minus_num(long):
	all = minus + num

	password = "".join(random.choices(all,k = long))

	return password


def generador_num_simb(long):
	all = num + simb

	password = "".join(random.choices(all,k = long))

	return password


def generador_minus_simb(long):
	all = minus + simb

	password = "".join(random.choices(all,k = long))

	return password

#-------- combinación de 3---------#

def generador_mayus_minus_numeros(long):
	all = mayus + minus + num

	password = "".join(random.choices(all,k = long))

	return password


def generador_mayus_numeros_simb(long):
	all = mayus + num +simb

	password = "".join(random.choices(all,k = long))

	return password

def generador_minus_numeros_simb(long):
	all = minus + num + simb

	password = "".join(random.choices(all,k = long))

	return password

def generador_mayus_minus_simb(long):
	all = mayus + minus + simb

	password = "".join(random.choices(all,k = long))

	return password
