
def caesar(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result

def vigenere(text,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    letra_index = dict(zip(alphabet, range(len(alphabet))))
    index_letra = dict(zip(range(len(alphabet)),alphabet))
    result = ""
    split_message = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    for each in split_message:
        i = 0
        for letra in each:
            numero =  (letra_index[letra] + letra_index[key[i]]) % len(alphabet)
            result  += index_letra[numero]
            i += 1
    return result


def rail_fence(text, key):
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)] 
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        rail[row][col] = text[i]
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
