import random
from words import words
import string

def valid_word(words):
    word=random.choice(words) #randomly chooses words from the list
    return word.upper()

def hangman():
    word=valid_word(words)
    word_letter=set(word) # letter in world
    alphabet=set(string.ascii_uppercase)# predermined list of upper case characters
    used_letters=set() # keeps track of the letters user has guessed
    num=0
    lives=6
    print("Genre is popular Tech Companies")
    while(len(word_letter)>0 and lives!=0):
        num+=1
        print('You Have',lives,'lives. Your Used letters are: ',' '.join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ',' '.join(word_list))
        # getting User Input
        user_letter=input("Guess Letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives-=1         # takes away a life if wrong
        elif user_letter in used_letters:
            print("You have already used that letter.Please try again ")
        else:
            print("Invalid Character. Please try again. ")
    if(lives!=0):
        print(f"Congrats u have guessed the word {word} in {num} tries")
    else:
        print(f"U have lost the game since no more lives are left. The word was {word}")
# gets here when length of word_letter==0
hangman()
