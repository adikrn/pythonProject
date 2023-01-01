import os

default_text = "This is sample text\nAnd second line\nAnd third line\n"
path = "C:\\Users\\adikr\\Desktop\\testfile.txt"
if os.path.exists(path):
    print("The location exists!")
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist")
    userInput = input("Do you want to creat it(y/n)?").lower()
    while (userInput != 'y' and userInput != 'n' ):
        userInput = input("Enter a valid choice!\nDo you want to create it(y/n)?").lower()
    if(userInput == 'y'):
        print("Default text for file:\n \"" + default_text + "\"")
        text = input("Enter new text or enter for no change:")
        if(text == ""):
            text = default_text
        try:
            with open(path, 'w') as file:
                try:
                    file.write(text)
                except Exception as e:
                    print("Error occured:\n" + e)
                else:
                    print("File written successfully at path:\n" + path)
            file.close()
        except Exception as e:
            print("Error occured:\n" + e)
    else:
        print("Alright!")

