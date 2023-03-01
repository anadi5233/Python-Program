# use open fuction to read the content of a file 
f = open('sample.txt', 'r')# by default the mode is r 
#data = f.read()
data = f.read(5)# it will read first five characters from the file 
print(data)
f.close()
