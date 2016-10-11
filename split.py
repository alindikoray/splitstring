def words(word_string):
      """initiates function that accepts string parameters to be counted"""
	word_list = word_string.split() #split the string
	word_count = {}
       #for each word in the line:
	for word in word_list:
		word = word.strip()
		if word.isdigit():
			word = int(word)
		if not word in word_count:
			word_count[word] = 1
	else:
	  word_count[word] += 1
	return word_count
	
print words("olly olly in come free")#print the string