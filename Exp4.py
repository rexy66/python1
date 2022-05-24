command = ""
indir1 = False
indir2 = False
indir3 = False


while True:

    command = input(">").lower()
    
    if command == "1":
        if indir1:
            print("You are already in directory 1!")
        else:
            indir1 = True
            indir2 = False
            indir3 = False
            print("DIRECTORY 1: \n to execute functions: a-func a b-funcb ")


    elif command =="2":
        if indir2:
            print("You are already in directory 2!")
        else:
            indir1 = False
            indir2 = True
            indir3 = False
            print("DIRECTORY 2:\n to execute functions:  a-func a b-funcb")
            
    elif command =="3":
        if indir3:
            print("You are already in directory 3!")
        else:
            indir1 = False
            indir2 = False
            indir3 = True
            print("DIRECTORY 3:\n to execute functions: a-func a b-funcb")


    elif command =="quit":
        break
    else:
        print("Sorry, i don't understand")

