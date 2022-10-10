import random
import time

#Global variables
my_string =input("Enter a string to encrypt: ")
my_key = []
my_list = []
encryption_list = []
decryption_list = []
plaintext_list = []

'''
This function uses the current system time to generate a random seed, then it iterates
over the string typed by the user and gives each index a random integer value between 0
and 255(the whole ASCII table)
'''
def key_generator():
    x = time.time()
    random.seed(x)
    for i in range(len(my_string)):
        my_key.append(random.randint(0, 255))
    return(my_key)

'''
This function takes in the string and generated key, then iterates over the string and
gets the ascii value for each index and appends it to a new list, then it iterates over
the new list and the key and performs an XOR function on each index, to which it appends
the value to the encryption_list. Then it converts the values into characters which
returns the cipher text.
'''
def encryption(my_string, my_key):
    for i in my_string:
        my_list.append(ord(i))
    for i in range(len(my_list)):
        for j in range(len(my_key)):
            x = (my_key[j] ^ my_list[i])
        encryption_list.append(x)
    secret_text = [chr(encryption_list[i])for i in range(0, len(encryption_list))]
    correct_list = ''.join([str(i) for i in secret_text])
    return(correct_list)

'''
this function takes in the key and encryption_list created in the previous function and
performs another XOR with them and then appends them to the decryption_list, then the
plaintext_list converts the the decryption_list back into characters and then joins them
in the my_list 
'''
def decryption(encryption_list, my_key):
    for i in range(0, len(encryption_list)):
        for j in range(len(my_key)):
            x =  (encryption_list[i] ^ my_key[j])
        decryption_list.append(x)
    plaintext_list = [chr(decryption_list[i])for i in range(0, len(decryption_list))]
    my_list = ''.join([str(i) for i in plaintext_list])
    return(my_list)

def main():
    key_generator()
    print("The original string is :", my_string)
    print("The encrypted string is: ", encryption(my_string, my_key))
    print("The decrypted string is: ", decryption(encryption_list, my_key))

main()

