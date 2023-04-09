import os

print("Insert your file name")
CharName = input()

try: 
    print("Looking for " + CharName)
    f = open(CharName + ".txt")
    print(f.read())
    f.close()
    wltEdit = input ("Would you like to Edit it?(y/n)")

except FileNotFoundError:
    print("Not Found")
    print("Would you like to Create {0}?(y/n)".format(CharName))
    wltCreate = input()

    if("y" in wltCreate.lower()):
        wltEdit = "y"
        pass

    elif("n" in wltCreate.lower()):
        exit()

except: 
    print("Something went wrong")

wpath = CharName + ".txt"

if ("y" in wltEdit.lower()):
    f = open(CharName + ".txt", "a+")
    Edit = input("Write down your next line\n")
    f.write("\n")
    f.write(Edit)
    f.close()
    f = open(CharName + ".txt","r")
    print(f.read())

elif("n" in wltEdit.lower()):
    Delete = input("It's your desire to delete {0}?(y/n)".format(CharName))

    if("y" in Delete.lower()):
        if os.path.exists(wpath):
            os.remove(wpath)
            print("Sucessfully deleted")

        else:
            print("File no longer avaliable")
            
    elif("n" in Delete.lower):
        print("Bye then")