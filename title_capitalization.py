import sys

title = input('Please type the title to capitalize: \n')

# special word which should not be capitalized while within a sentence
special_list = ['a', 'the', 'to', 'at', 'in', 'with', 'and', 'but', 'or']

# Split the title string by spaces
words = title.split(' ')

# len(word)-1 in the for loop ensure that the first and last word are not affected
for i in range(len(words)-1):

    # Capitalize the first and last word
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()

    # Lowercase words in the special list
    if words[i].lower() in special_list:
        words[i] = words[i].lower()
    # Capitalize words that aren't in the special list
    else:
        words[i] = words[i].capitalize()
    i +=1

# finally joins all the words with a space and print it to the user
print(' '.join(words))

