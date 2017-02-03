# import sys
#
# title = input('Input the title to capitalize')

title = 'wHY DoeS A biRd Fly To The bush'

# special word which should not be capitalized while within a sentence
special_list = ['a', 'the', 'to', 'at', 'in', 'with', 'and', 'but', 'or']

# Split the title string by spaces
words = title.split(' ')

# Capitalize the first and last word
words[0] = words[0].capitalize()
words[-1]= words[-1].capitalize()

# len(word)-1 in the for loop ensure that the first and last word are not affected
for i in range(len(words)-1):

    if words[i].lower() in special_list:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].capitalize()
    i +=1

print(' '.join(words))

