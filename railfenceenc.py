def railfenceEnc(key, plain):
    plain = plain.upper()
    cipherText = ""
 
    # filling the "railfence" grid with all zeroes using dimensions
    height = key
    width = len(plain)
    box = [[0 for x in range(width)] for y in range(height)]
 
    # filling the "railfence" grid with characters of the plaintext
    up = False # indicates the direction of "zigzag"
    ind = 0 # indicates the height index
    for i in range(len(plain)):
        box[ind][i] = plain[i]
        # height index changes based on direction
        ind=ind-1 if up else ind+1
        # switch directions if we are at the top or bottom
        if ind==0 or ind==key-1:
            up = not up
 
    # add all non-zero elements of the railfence to the ciphertext
    for h in range(height):
        for w in range(width):
            if box[h][w] != 0:
                cipherText += box[h][w]
 
    return cipherText
