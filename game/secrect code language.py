import random
import string
print("Secrect letter generator ")
print("(*)Enter 0 to decode the letter   (*)Enter 1 to code the letter ")
convert = int(input("Enter 0 or 1 to genarate : "))

#To genarate random string at first and last part of string
def randomstring(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

match convert:
    # 0 : to convert a letter to secreate code
    case 0:
        to_decode = input("Enter letter to decode : ")
        words = to_decode.split() # Split the passage into words
        newword = []
        for word in words:
            if len(word)>2:
                first = randomstring(3)
                last = randomstring(3)
                con_word = first + word[1:] + word[0] + last  # word[1:] refer to index 1 to end  
                newword.append(con_word)
            else:
                newword.append(word[::-1]) # Shortcut to reverse a string
            
        print(" ".join(newword))
        
    # 1 : to convert a code to letter
    case 1:
        to_encode = input("Enter letter to encode : ")
        words = to_encode.split() # Split the passage into words
        newword = []
        for word in words:
            if len(word)>2:
                con_word = word[-4] + word[3:-4] # word[-4] refere to last 4th index of word &&  word[3:-4] refer to 3rd to last 4th index of word
                newword.append(con_word)
            else:
                newword.append(word[::-1]) # Shortcut to reverse a string
            
        print(" ".join(newword))
                
                
                
                
                
                





