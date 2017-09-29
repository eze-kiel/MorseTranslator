while True:

	# obtenir une phrase
	original = input("Ecris la phrase: ")
	# spliter la phrase
	lettres = list(original)
	# trouver l'équivalence fr/morse
	morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
			'.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..--', '...-',
			'.--', '-..-', '-.--', '--..']
	newSentence = []


	for lettre in lettres:
		if lettre == " ":
			newWord = " "
			newSentence.append(newWord)
		elif lettre == "'":
			newWord = " "
			newSentence.append(newWord)
		elif lettre == ",":
			newWord = ","
			newSentence.append(newWord)
		else:
			rang = ord(lettre) - 97
			lettre = morse[rang]
			newWord = lettre
			newSentence.append(newWord)


	# reformer la phrase en morse
	output = " ".join(newSentence)
	# l'afficher
	print("{} s'écrit {} en morse !".format(original,output))
