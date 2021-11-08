f = open('horse_ebooks.txt', 'r')
text = f.read()
print(text)

def read_file(filename):
    '''Returns the text contained in file with given filename.'''
    f = open(filename, 'r')
    text = f.read()
    return text

def pig_latin(word):
    '''Returns the pig latin translation of a word.'''
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    i = 0
    while not (word[i] in vowel_list):
    	letter = word[i]
    	new_word = word[1:]
    	new_word = new_word + letter
    	i += 1
    return new_word + 'ay'

#print(pig_latin('Hello'))
        
def izzle(word):
	'''Returns the izzle translation of a word.'''
	i = 0
	temp = word
	new_word = word
	vowel_list = ['a', 'e', 'i', 'o', 'u']
	word_list = [x for x in word]
	word_list_only_vowels = [x for x in word_list if x in vowel_list]
	if len(word_list_only_vowels) > 1:
		while not word[-i-1] in vowel_list:
			new_word = temp[:-1]
			temp = new_word
			i += 1
		return (new_word[:-1] + 'izzle')
	else: 
		return 'izzle'
#print(izzle('Shizzle'))
#print(izzle('my'))
#print(izzle('and'))


def hello_langauge_game(languageGame):
	return languageGame('hello')

def apply_language_game(text, language_game):
	'''Takes a text and a language_game function as inputs'''
	'''Returns the language game function applied to every word of the text.'''
	word_list = text.split()
	change = [language_game(x) for x in word_list]
	return ' '.join(change)

#text = read_file('gettysburg.txt')
#print(apply_language_game(text, izzle))

def count_words(text):
	word_list = text.split()
	dict = {}
	for i in range(len(word_list)):
		word = word_list[i]
		if word in dict:
  			dict[word] = dict[word] + 1
		else:
  			dict[word] = 1
	return dict

text = read_file('horse_ebooks.txt')
#print(count_words(text)) 

text = read_file('horse_ebooks.txt')
counts = count_words(text)
#print(sorted(counts, key = counts.get, reverse = True))

def top_n_words(counts, n):
	original_list = sorted(counts, key = counts.get, reverse = True)
	return original_list[:n]

#print(top_n_words(counts, 5))

def print_top_n_words(counts, n):
	top_list = sorted(counts, key = counts.get, reverse = True)
	top_list_value = sorted(counts.values(), reverse = True)
	for i in range(n):
		print(top_list[i] + ' ' + str(top_list_value[i]))

#print_top_n_words(counts, 5)

def average_word_length(counts):
	value_list = list(counts.values())
	keys_list = list(counts.keys())
	for i in range(len(counts)):
		total_letters = len(keys_list[i]) * value_list[i]
		total_words = sum(value_list)
		return total_letters/ total_words
#print(counts.values())
print(average_word_length(counts))

def word_diversity(text):
	word_list = text.split()
	word_unique = set(word_list)
	print(word_unique)
	total_unique_words = len(word_unique)
	total_words = len(text)
	print(total_words)
	return total_unique_words/ total_words

text = read_file('horse_ebooks.txt')
print(len(text))
print(word_diversity(text))
