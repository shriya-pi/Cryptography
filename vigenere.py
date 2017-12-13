def vigenere(key, plain):

  #setting the plaintext and key to be all uppercase for simplicity
  plain = plain.upper()
  key = key.upper()
  
  cipherText = ""
  
  for i in range(len(plain)):
    currentP = ord(plain[i])
    currentK = ord(key[i%(len(key))])
    
    if not (currentP < 65 and currentP > 90):
      if (currentP + currentK) < 156:
        newChar = chr(currentP + currentK - 65)
      else:
        newChar = chr(currentP + currentK - 91)
        
      cipherText += newChar
  
  return cipherText
