#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This functions check for vowels in entered string and return True/False
def vowelcheck(x):
	v = ["a", "o", "u", "å", "e", "i", "y", "ä", "ö"]
	for i in v:
		if i == x:
			return True
#TODO: Traditional Finnish nouns does not conjugate correctly e.g. Hauki should be hauen and not haukin
#TODO: Change this to regex
def main(x):
	lista = []
	#No point in making it a list as one can check the last letter with a_string[-1]
	for i in x:
		lista.append(i)
	# does the noun end with a vowel?
	if vowelcheck(lista[-1]) == True:
		# then check if nk in the end of the verb stem
		if lista[-3] == "n" and lista[-2] == "k":
			lista[-2] = "g"
			print("".join(lista) + "n")
		# then check if mp in the end of the verb stem
		elif lista[-3] == "m" and lista[-2] == "p":
			lista[-2] = "m"
			print("".join(lista) + "n")
		# then nt
		elif lista[-3] == "n" and lista[-2] == "t":
			lista[-2] = "n"
			print("".join(lista) + "n")
		# then lt
		elif lista[-3] == "l" and lista[-2] == "t":
			lista[-2] = "l"
			print("".join(lista) + "n")
		# then rt
		elif lista[-3] == "r" and lista[-2] == "t":
			lista[-2] = "r"
			print("".join(lista) + "n")
		# then pp
		elif lista[-3] == "p" and lista[-2] == "p":
			lista[-2] = ""
			print("".join(lista) + "n")
		# then tt
		elif lista[-3] == "t" and lista[-2] == "t":
			lista[-2] = ""
			print("".join(lista) + "n")
		# then kk
		elif lista[-3] == "k" and lista[-2] == "k":
			lista[-2] = ""
			print("".join(lista) + "n")
		# then ht
		elif lista[-3] == "h" and lista[-2] == "t":
			lista[-2] = "d"
			print("".join(lista) + "n")
		# then t to d
		elif vowelcheck(lista[-3]) and lista[-2] == "t":
			lista[-2] = "d"
			print("".join(lista) + "n")
		# then k to ""
		elif vowelcheck(lista[-3]) == True and lista[-2] == "k":
			lista[-2] = ""
			print("".join(lista) + "n")
		else:
			print("".join(lista) + "n")

	
	if lista[-3] == "g" and lista[-2] == "a" and lista[-1] == "s":
		lista[-3] = "k"
		lista[-1] = "a"
		print("".join(lista) + "n")
	if lista[-1] == "s":
		lista[-1] = "k"
		lista.append("s")
		lista.append("e")
		print("".join(lista) + "n")
	if lista[-1] == "n":
		lista[-1] = "m"
		lista.append("e")
		print("".join(lista) + "n")
		
	

while True:
    UserInput = input("Write a Finnish noun or type exit to end: ")
    if UserInput == "exit":
      break;
    main(UserInput)
