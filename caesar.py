def caesar(key, plain):

  #setting the plaintext to be all uppercase for simplicity
  plain = plain.upper()
  
  #defining a blank ciphertext to be returned
  cipherText = ""
  
  for i in range(len(plain)):
    new = ord(plain[i]) + key
    #check if the new character is still a letter
    if new >= 65 and new <= 90:
      cipherText += chr(new)
    else:
      ciphetText += chr(new-26)
      
  return cipherText
