def columnar(key, plain):
    # setting the plaintext and key to be all uppercase for simplicity
    plain = plain.upper()
    key = key.upper()
    #defining a blank ciphertext string to be returned
    cipherText = ""
 
    #setting up the dimensions of the grid
    height = len(plain) / len(key) + 1
    width = len(key)
    box = [[0 for x in range(width)] for y in range(height)]
 
    # fill the grid with the letters of the plaintext
    for h in range(height):
        for w in range(width):
            if w + h * len(key) >= len(plain):
                break
            box[h][w] = plain[w + h * len(key)]
 
    # changing the key into a list with corresponding numeric entries
    key = [ord(key[i]) - 64 for i in range(len(key))]
 
    # creating a list the length of the keyword and filling it with the numbers corresponding to alphabetical order
    numsOrd = [0] * len(key)
    for y in enumerate(sorted((tuple(reversed(x)) for x in enumerate(key)))):
        numsOrd[y[1][1]] = y[0]
 
    # adding the letters in each column in the order indicated by numOrd
    for i in range(len(out)):
        ind = out.index(i)
        for j in range(height):
            if box[j][ind] != 0:
                cipherText += box[j][ind]
 
    return cipherText
