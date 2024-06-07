#ASCII value for the first valid alphabet
firstAlphaCode=ord("A")
#ASCII value for the last valid alphabet
lastAplhaCode=ord("Z")
#range of alphabets in ASCII
alphaRange=lastAplhaCode-firstAlphaCode+1

def caesarCipher(message, shiftKey):
    #result holder
    cipherMessage=""
    #working only with uppercase
    for letter in message.upper():
        #checking if alphabet or not
        if letter.isalpha():
            #gets the ASCII value of each letter
            letterCode=ord(letter)

            #gets the ASCII value for each letter of ciphertext
            newLetterCode=letterCode+shiftKey

            #reduces range of alphabets, to keep alphabets only
            if(newLetterCode>lastAplhaCode):
                newLetterCode-=alphaRange
            

            if(newLetterCode<firstAlphaCode):
                newLetterCode+=alphaRange

            #gets the letter from the new ASCII value of ciphertext
            cipherText=chr(newLetterCode)

            #stores valid letters for cipher in final ciphertext message
            cipherMessage=cipherMessage+cipherText
        else:
            #stores weird symbols in ciphertext
            cipherMessage=cipherMessage+letter

    #prints the final cipher
    print(cipherMessage)

originalMessage=input("Please enter the message to be Encrypted/Decrypted: ")
key=int(input("Please enter your Encryption/Decryption key(absolute): "))

choose=int(input("Enter 1 for Encryption, Enter 2 for Decryption: "))
if(choose == 1):
    caesarCipher(originalMessage, abs(key))
elif(choose == 2):
    caesarCipher(originalMessage, -abs(key))
else:
    print("Invalid choice. Please enter 1 or 2.")