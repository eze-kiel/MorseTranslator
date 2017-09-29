while True:

	# obtenir une phrase
	original = input("Write your sentence: ")
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
	print("{} is {} traduced in morse !".format(original,output))
