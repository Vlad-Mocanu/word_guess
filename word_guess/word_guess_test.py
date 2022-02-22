#/bin/python3

import sys, os
import word_guess
from random import choice
from collections import OrderedDict

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def provide_clues(word_to_guess, picked_word):
    clues = []
    for letter_index in range(0, word_guess.word_length):
        if picked_word[letter_index] == word_to_guess[letter_index]:
            clues.append('c')
            picked_word = picked_word.replace(picked_word[letter_index], '@', 1)
        elif picked_word[letter_index] in word_to_guess:
            clues.append('m')
        else:
            clues.append('w')
    return clues

def progres(count, total, status='', bar_len=60):
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    fmt = '[%s] %s%s ...%s' % (bar, percents, '%', status)
    print('\b' * len(fmt), end='')  # clears the line
    sys.stdout.write(fmt)
    sys.stdout.flush()

if __name__ == '__main__':
    fixed_length_words = word_guess.get_words_from_file()
    performance = OrderedDict()
    
    for word_index in range(0,int(len(fixed_length_words)/100)):
        progres(word_index, int(len(fixed_length_words)/100) - 1, '%d/%d' % (word_index, int(len(fixed_length_words)/100) - 1))
    
        word_to_guess = fixed_length_words[word_index]
        words_list = fixed_length_words;
        
        blockPrint()
        print("Picked word to be guessed: %s" % (word_to_guess))

        iteration = 1
        while len(words_list) > 1:
            print('Iteration %d' % (iteration))
            picked_word = word_guess.pick_word(words_list)
            clues = provide_clues(word_to_guess, picked_word)
            #print ('The clues are: ' + ' '.join(clues))
            words_list = word_guess.react_on_clues(words_list, picked_word, clues)
            iteration = iteration + 1
        
        print('Victory in %d iterations with word %s' % (iteration, words_list[0]))
        performance[words_list[0]] = iteration
        enablePrint()
    
    print()
        
    performance_list = list(performance.values())
    hist = word_guess.histogram(str(x) for x in performance_list)
    hist = sorted(hist.items(), key=lambda item: item[0])
    print(hist)
