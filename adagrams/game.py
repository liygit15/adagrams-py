from random import randint

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 
    'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 
    'Y': 2, 'Z': 1
}

def draw_letters():
    letter_list = []
    hand = []

    for letter in LETTER_POOL:
        letter_list += [letter] * LETTER_POOL[letter]

    for i in range(10):
        random_num = randint(0, len(letter_list) - 1)
        alpha = letter_list[random_num]
        hand += [alpha]
        letter_list = letter_list[:random_num] + letter_list[random_num + 1:]

    return hand


def uses_available_letters(word, letter_bank):
    copy_of_letter_bank = letter_bank[:]

    for letter in word.upper():
        if letter not in copy_of_letter_bank:
            return False
        
        for i in range(len(copy_of_letter_bank)):
            if letter == copy_of_letter_bank[i]:
                copy_of_letter_bank = copy_of_letter_bank[:i] + copy_of_letter_bank[i + 1:]
                break

    return True      


SCORE_POOL = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 
    'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 
    'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

def score_word(word):
    total = 0

    for letter in word.upper():
        total += SCORE_POOL[letter]

    if len(word) >= 7:
        total += 8

    return total
        

def get_highest_word_score(word_list):
    max_score = 0
    best_word = word_list[0]
    
    for word in word_list:
        score = score_word(word)

        # Get the highest score among the words.
        if score > max_score:
            max_score = score
            best_word = word
        # Deal with tie situations.
        elif score == max_score:
            # If the word is the first one whose length is 10, it's best word.
            if len(word) == 10 and len(best_word) != 10 :
                best_word = word
            # Otherwise，the shortest, the best.
            elif len(word) < len(best_word) and len(best_word) != 10:
                best_word = word

    return(best_word, max_score)
    
