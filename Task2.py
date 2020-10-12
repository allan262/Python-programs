f=input("Input the Filename: ")
x=f.split(".")
y=x[-1]
if(y=="py"):
    z=("Python")
elif(y=="txt"):
    z=("Text file")
elif(y=="docx"):
    z=("Word file")
else:
    z=("INVALID")


print("The extension of the file is: ",z)
