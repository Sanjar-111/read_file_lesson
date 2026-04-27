#Rread file and convert to list
def read_file():
    s=open("data.txt","r")
    a=s.read()
    a=a.split(",")
    return a
print(read_file())

#Print list from file
