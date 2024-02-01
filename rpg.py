myStuff = []

f = open("Stuff.mine", "r")
myStuff = eval(f.read())
f.close()

while True:
  print("RPG Inventory\n")
  user_input = input("1: Add  2: Remove  3: View  > ")

  try:
    if user_input == "1":
      item = input("Input the item to add: > ").capitalize()
      myStuff.append(item)
      print(f"{item} has been added to your inventory.")
    elif user_input == "2":
      item = input("Input the item to remove: > ").capitalize()
      if item in myStuff:
        myStuff.remove(item)
        print(f"{item} has been removed from your inventory.")
      else:
        print("You don't have that item.")
    else:
      item = input("Input the item to view: > ").capitalize()
      print(f"You have {myStuff.count(item)} {item}")
    break

  except Exception as err:
    print("You must input a numerical character, try again.\n" + err)
    continue

f = open("Stuff.mine", "w")
f.write(str(myStuff))
f.close()
