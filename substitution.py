def substitution(key, plain):
  
  #setting the plaintext and key to all uppercase for simplicity
  plain = plain.upper()
  key = key.upper()
  
  #defining a blank cipher alphabet and ciphertext string
  cipherAlphabet = []
  cipherText = ""
  
  #set the first part of the cipher alphabet as the keyword
  for i in range(len(key)):
    cipherAlphabet.append(key[i])
    
  #setting the rest of the cipher alphabet
  for i in range(26):
    nextChar = chr(65 + i)
    if nextChar in cipherAlphabet:
      continue
    cipherAlphabet.append(nextChar)
    
  #encrypting the plaintext
  for i in range(len(plain)):
    plainIndex = ord(plain[i]) - 65
    cipherText += cipherAlphabet[plainIndex]
    
  return cipherText
