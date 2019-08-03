#Create and write in the file

text_file = open("file.txt","w")
text = "Hello world file"
text_file.write(text)
text_file.close()

# Append information

text_file = open("file.txt","a")
text = "\nHello world second line\nHelo world Third line"
text_file.write(text)
text_file.close()

# Load all the text in a string

text_file = open("file.txt","r")
text = text_file.read()
text_file.close()
print(text)

# Load the file in an array

text_file = open("file.txt","r")
text = text_file.readlines()
text_file.close()
print(text)

# From which character do you want to read

text_file = open("file.txt","r")
text_file.seek(17)
text = text_file.read()
text_file.close()
print(text)
# OR
text_file = open("file.txt","r")
text = text_file.read(17)
text_file.close()
print(text)


text_file = open("file.txt","r+")
text_list = text_file.readlines()
text_list[1] = "--------overwrite----------\n"
text_file.seek(0)
text_file.writelines(text_list)
text_file.seek(0)
text = text_file.read()
print(text)
text_file.close()

# BEST PRACTICE

with open("file.txt","r") as text_file:
    data = text_file.read()
    print(data)

# w = write
# r = read
# r+ = read and append
# a = append