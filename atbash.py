def atbash(plain):

  #setting the plaintext to be all uppercase for simplicity
  plain = plain.upper()
  
  #defining a blank ciphertext to be returned
  cipherText = ""
  
  for i in range(len(plain)):
    #only add characters that are letters
    if ord(plain[i]) >= 65 and ord(plain[i]) <= 90:
      cipherText += chr(155 - ord(plain[i]))
      
  return cipherText
