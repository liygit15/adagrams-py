from random import randint
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letter_list = []
    guess_list = []
    copied_letter_pool = {}
    for key in LETTER_POOL:
        copied_letter_pool[key] = LETTER_POOL[key]
        letter_list.append(key)
    for i in range(10):
        random_num = randint(0,len(letter_list)-1)
        alpha = letter_list[random_num]
        guess_list += alpha
        copied_letter_pool[alpha] -= 1
        if copied_letter_pool[alpha] == 0:
            letter_list.remove(alpha)
    return guess_list
    
    

def uses_available_letters(word, letter_bank):
    copy_of_letter_bank = []
    for _ in letter_bank:
        copy_of_letter_bank += _
    
    actual_word = word.upper()
    for i in actual_word:
        if i not in copy_of_letter_bank:
            return False
        else:
            copy_of_letter_bank.remove(i)
    return True      

def score_word(word):
    score_pool = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
    total = 0
    actual_word = word.upper()
    if word == "":
        return 0
    for letter in actual_word:
        total += score_pool[letter]
    if len(actual_word) >= 7:
        total += 8
    return total
        

def get_highest_word_score(word_list):
    word_score = {}
    max_score = 0
    highest_score_list = []
    best_word_list = []
    longest = ''
    longest_list = []

    for string in word_list:
        word_score[string] = score_word(string)
    for i in word_score:
        if word_score[i] > max_score:
            max_score = word_score[i]
    for word in word_score:
        if word_score[word] == max_score:
            highest_score_list += [word]
            # highest_score_list.append(i)
    if len(highest_score_list) == 1:
        best_word = highest_score_list[0]
        return (best_word,max_score)  
    
    for i in highest_score_list:
        if len(i) == 10:
            return (i,max_score)
    
    best_word = highest_score_list[0]          
    for index in range(len(highest_score_list) - 1):
        if len(highest_score_list[index]) == len(highest_score_list[index + 1]):
            highest_score_list.remove(highest_score_list[index + 1])
        elif len(highest_score_list[index]) < len(highest_score_list[index + 1]):
            best_word = highest_score_list[index] 
        elif len(highest_score_list[index]) > len(highest_score_list[index + 1]):
            best_word = highest_score_list[index + 1]
    return (best_word,max_score)   
        