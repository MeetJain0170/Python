import os

print("Script is running...")  # Debugging

if os.path.exists("wordlist.txt"):
    print("wordlist.txt found!")
else:
    print("Error: wordlist.txt NOT found!")

with open("wordlist.txt", "r") as f:
    content = f.read()
print("File content:", content)  # Debugging

def load_words():
    with open('wordlist.txt', 'r') as file:  
        words_list = [word.strip() for word in file.readlines()]
    
    print("Loaded words:", words_list)  # Debugging print
    return words_list

load_words()
