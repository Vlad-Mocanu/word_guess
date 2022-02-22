#/bin/python3

from collections import OrderedDict

word_length = 5

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.read().split()

    return valid_words
    
def histogram(word_list):
    hist = OrderedDict()
    for word in word_list:
        for char in word:
            if char not in hist:
                hist[char] = 1
            else:
                hist[char] += 1
    return hist
    
def pick_word(word_list):
    print(word_list)
    for letter_index in range(0, word_length):
        if len(word_list) > letter_index:
            used_key = list(histogram(word_list).keys())[letter_index]
            print('First key for %d is %s' % (letter_index, used_key))
            word_list = [x for x in word_list if used_key in x]
    print('Picking a word (from %d words with most frequent letters): %s' % (len(word_list), word_list[0]))
    return word_list[0]
    
def get_clues():
    letter_index = 0
    clues = []
    print('Type W(rong)/M(isplaced/C(orrect) for each letter')
    while letter_index < word_length:
        value = input('Letter[%d] = ' % letter_index)
        if value.lower() in ['w', 'm', 'c']:
            clues.append(value.lower())
            letter_index = letter_index + 1
    
    return clues

def react_on_clues(word_list, used_word, clues):
    for letter_index in range(0, word_length):
        letter = used_word[letter_index]

        if clues[letter_index] == 'w':
            has_misplaced = 0
            not_occurances = []
            for i in range(0, word_length):
                #if there is another letter like it and it's misplaced we exclude only the wrong position
                if used_word[i] == letter:
                    if clues[i] == 'm':
                        has_misplaced = 1
                    elif clues[i] == 'w':
                        not_occurances.append(i)
                else:
                    not_occurances.append(i)
    
            if has_misplaced:
                #exclude only the wrong position
                word_list = [x for x in word_list if x[letter_index] != letter]             
                print('Letter %s is not used but there is anoter misplaced one, new word_list size %d' % (letter, len(word_list)))
            else:
                #exclude the possitions of where there aren't occurances
                for i in not_occurances:
                    word_list = [x for x in word_list if x[i] != letter]
                print('Letter %s is not used, new word_list size %d' % (letter, len(word_list)))
                
        elif clues[letter_index] == 'c':
            word_list = [x for x in word_list if x[letter_index] == letter]
            print('Letter %s is on correct position, new word_list size %d' % (letter, len(word_list)))
            
        elif clues[letter_index] == 'm':
            word_list = [x for x in word_list if x[letter_index] != letter and letter in x]
            print('Letter %s is misplaced, new word_list size %d' % (letter, len(word_list)))
    
    return word_list
    
def get_words_from_file():
    english_words = load_words()
    print('Loaded %d words from file' % (len(english_words)))
    fixed_length_words = [x for x in english_words if len(x) == word_length]
    print('Extract words with length %0d, there are %d words' % (word_length, len(fixed_length_words)))
    
    return fixed_length_words

if __name__ == '__main__':
    fixed_length_words = get_words_from_file()

    iteration = 1
    while len(fixed_length_words) > 1:
        print('Iteration %d' % (iteration))
        pick_word(fixed_length_words)
        picked_word= input('Picked_word = ')
        clues = get_clues()
        fixed_length_words = react_on_clues(fixed_length_words, picked_word, clues)
        iteration = iteration + 1
    
    print('Victory in %d iterations with word %s' % (iteration, fixed_length_words[0]))
