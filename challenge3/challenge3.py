change = 'http://www.pythonchallenge.com/pc/def/{solution}.html'

font = open('text.txt', 'r')
text = font.read()

# Extract alphabet characters from file content
#isalpha distinguishes letters of symbols
#therefore discrimiante all symbols that are not letters
solution = ''.join([letter for letter in text if letter.isalpha()])

print (solution)


#this is a method whit use change the word, in the URL
"""
url = change.format(solution=solution)
"""
