
#message store string to be encrypted or decrypted

#dictionary for the morse code chart
ENG_TO_MORSE = {'a':'.-' , 'b':'-...' , 'c':'-.-' ,
                'd':'-..' , 'e':'.' , 'f':'...-' ,
                'g':'--.' , 'h':'....' , 'i':'..' ,
                'j':'.---' , 'k':'-.-' , 'l':'.-..',
                'm':'--' , 'n':'-.' , 'o':'---' , 
                'p':'.--.' , 'q':'--.-' , 'r':'.-.' ,
                's':'...' , 't':'-'  , 'u':'..-' ,
                'v':'...-' , 'w':'.--' , 'x':'-..-' ,
                'y':'-.--' , 'z':'--..' , '1':'.----' ,
                '2':'..---' , '3':'...--' , '4':'....-',
                '5':'.....' , '6':'-....' , '7':'--...' ,
                '8':'---..' , '9':'----.' , '0':'-----'}

#defined function that encrypts using the morse code chart
def eng_to_morse(text):
    #stores the morse code translated from english
    eng_trans = ''
    for letter in text:
        if letter != ' ':
            #goes through the dictionary and replaces letters
            # with the corresponding morse code
            # along with a space to separate
            # morse codes for different characters
        
            eng_trans += ENG_TO_MORSE[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 spaces indicate different words
            eng_trans += ' '
    return eng_trans

#defined function that decrypts 
# morse to english using the ENG_TO_MORSE dictionary
def morse_to_eng(text):
    
    #extra space added at the end to access the last morse code

    text += ' '
    #stores the english text translated from morse code
    decrypted = ''
    #stores morse code of a single character
    single_char = ''
    for letter in text:
        #checks for spaces
        if (letter != ' '):
            #keepss count of spaces
            i = 0
            #storing morse of single character
            single_char +=letter
        #if there is a space    
        else:
            #if i = 1 its a new character 
            i+= 1
            #if i = 2 its a new word
            if i==2:

                #adding space bbetween words
                decrypted += ' '
            else: 

                #aaccessing the keys using their values (decryption)
                decrypted += list(ENG_TO_MORSE.keys())[list(ENG_TO_MORSE.values()).index(single_char)]
                single_char = ''

    return decrypted 


#runs the rest of the code depending on the users decision of encrypting or decrytpting
def run():
        #stores whether the user wants to encrypt or decrypt
        DEC=input("Choose encrypting or decyrpting: (e/d) ")
        #differentiates between user input
        if DEC== 'e':
            #saves the user input as a string
            message = str((input("input message: ")))
            #gets the translated text from the encrypting function in lower case
            result = eng_to_morse(message.lower())
            #prints result
            print(result)

        else:
            
            if DEC == 'd':
                #saves the input in a string format
                message = str((input("input cipher: ")))
                #saves the result of the decrytping
                result= morse_to_eng(message)
                #prints result
                print(result)
            else: 
                #if the input was neither 'e' or 'd' prints the following text
                print("invalid input")



    
                       

#executes run function
run()




