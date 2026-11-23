# Q.3: File Reading with else Block

try:
    fname = input("Enter a File name (with Extension) : ")
    with open(fname,"r") as file:
        content = file.read()

except FileNotFoundError as e:
    print("Error : File Not Founded!",e)
except OSError:
    print("Error : An Error occured while reading.")

else:
    print("File Content : \n",content)