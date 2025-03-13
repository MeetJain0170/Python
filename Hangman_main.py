#HANGMAN
import random

def load_words():
    with open('wordlist.txt', 'r') as file:  
        words_list = [word.strip() for word in file.readlines()]
    if not words_list:
        print("Error: wordlist.txt is empty!")
        return []
    return words_list
    
def choose_word(words_list):
    return random.choice(words_list)

def hangman():

    words_list = load_words() 
    word = choose_word(words_list) 
    word_length=len(word) 
    display = ['_' for i in word]
    print(display)
    tries=int(input("Enter the number of tries you need: "))
    guess_array=[]
    while tries > 0:
            
            guess = input("Guess a Letter: ").lower()
            print()  
            
            if guess in guess_array:
                print("Letter already guessed")
                continue   
            guess_array.append(guess) 

            for position in range(word_length):
                letter=word[position]
                
                if letter == guess:
                    display[position]=letter
            
            if guess not in word:
                tries-=1
            
            print(display)            
            print("tries left: " + str(tries))
            
            if '_' not in display:
                print("Dhinchak Dhinchak")
    
    if tries == 0:
        print("So sad the word was "+word)

hangman()