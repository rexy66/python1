
def make_list():
    num_of_items = int(input("how many items are there in this list?"))
    for i in range (num_of_items):
        append.(input("type in numbers"))
        
def get_ave():
    print("get average")
    
def clear_list():
    print("clear list")





while True:
   print ("M for Make list. X to quit.")
   print("A to get average Y to clear list")
   
   command = input(">").lower()
   nums = []
   
   if command == "m":
     make_list()
   elif command == "x":
     break
   elif command == "a":
     get_ave()
   elif command == "y":
     clear_list()
   else:
     print ("Invalid input")
     continue
