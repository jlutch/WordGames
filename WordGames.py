list = []
with open("ScrabbleDict.txt",'r') as f:
	for line in f:
		line = line.strip()
		for word in f:
			word = word.strip()
			if line != word[0:len(line)]:
				print(line)
				print(word[0:len(line)])
				list.append(word)
#print(list)






