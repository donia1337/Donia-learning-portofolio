# Given a word as input, output a list, containing only the letters of the word that are not vowels.
# The vowels are a, e, i, o, u.
print('Enter any word to get a list of the letters of the word that are not vowels')
word = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]
a=[i for i in word if i not in vowels ]
print(a)