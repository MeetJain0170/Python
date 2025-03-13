alphabet='abcdefghijklmnopqrstuvwxyz'
def caeser_cypher(text,shift,direction):
    result=""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction=='encode':
                new_posi = (position+shift)%26
            elif direction=='decode':
                new_posi = (position-shift)%26
            result+=alphabet[new_posi]
        else:
            result+=char
    return result

def cypher():
    direction=(input("Enter 'encode' if you want to encrypt or 'decode' if you want to decrypt a text: ")).lower()
    
    if direction not in ['encode','decode']:
        print(f"Not a valid command '{direction}'e it should be either encode or decode")
        return

    shift=int(input(f"Enter the amount by which you have to shift the letters in the {direction}: "))
    text=(input(f"Enter the text you want to {direction}: ")).lower()

    if direction in ['encode','decode']:
        result=caeser_cypher(text,shift,direction)
        print(f"the {direction}d text is {result}")
cypher()

            