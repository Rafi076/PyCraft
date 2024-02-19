# a file name "myfile.txt"

# f = open('myfile.txt','r')
# text = f.read()
# print(text) # Hello rafi you are awesome!!
# f.close()

# f = open('myfile.txt','w')
# f.write("Hello world\n") # Hello world 
# f.close()

# its important to close a file after you are done with it.
# this releases the resources used by the file and allows other 
# program to acess it. alternatively, you can use the with statement to autometically close 
# the file after you are done with it.
# Example:#
# with open('myfile.txt','a') as f: # a : append mood
#     f.write("Hey i'm rafii.The awesome!\n")

# f = open('number.txt','r')
# i = 0 
# while True:
#     i = i+1
#     line = f.readline()
#     if not line: 
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Mark of student {i} in Math is: {m1}")
#     print(f"Mark of student {i} in English is: {m2}")
#     print(f"Mark of student {i} in Bio is: {m3}")
#     print(line)
    
    

#in python, the seek() AND tell() are used to work with file object
# and thier position within a fike, these function are part of the 
# builtin io module, which provides a consistances interface for reading and writing 
# various file like objects,succh as files,pipes, and in-memory buffer.
# 
# the seek() function allow to move rhe current position within a file to a
# specific point. the position is specifiv is specified in bythes and you can move 
# either forward or backword from the current position for example:#

# let a file name "myfile.txt". to print first 5bytes of the txt file.
with open('myfile.txt','r') as f:
    f.seek(0) # move to the 0th byte in the file
    # to see where we start seek,we use tell()
    print(f.tell()) # 0
    # read the next 5 bytes
    data = f.read(5) # Hello
    print(data)
# tell() function returns the current position within the file, in bytes.this can usefull for keeping track of your location within file
