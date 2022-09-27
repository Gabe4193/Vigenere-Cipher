#Gabriel Wallace
#Vigenere Encrypt and Decrypt
 
# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text

#This function also creates the my_key.html file.
def generateKey(string, key):

    #print("ONE")
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    file = open("my_key.html", "w")
    file.write("".join(key))
    file.close()
    return("" . join(key))
     
# This function returns the
# encrypted text generated
# with the help of the key

#This function also creates an html file for the key.
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        if string[i].isalpha() == True or string[i] == " ":
            if string[i] == " ":
                cipher_text.append(chr(32))
            else:
                x = (ord(string[i].upper()) + ord(key[i])) % 26
                x += ord('A')
                cipher_text.append(chr(x))
    file = open("my_encryption.html", "w")
    file.write("". join(cipher_text))
    return("" . join(cipher_text))
     
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isspace():
            orig_text.append(" ")
        else:
            x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
    return("" . join(orig_text))

#This function is to read an html file
def htmlRead():
    file = open(input("Enter exact file name including extension to encrypt: "), "r")
    fileRead = file.read()
    file.close()
    return fileRead
    
# Driver code
if __name__ == "__main__":
    string = htmlRead()
    keyword = input("Choose a keyword: ")
    key = generateKey(string, keyword)
    file = open("my_key.html", "r")
    keyFile = file.read()
    cipher_text = cipherText(string,keyFile)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))
 
# The code is contributed by Pratik Somwanshi and modified by Gabriel Wallace
