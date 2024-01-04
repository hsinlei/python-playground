todoList = []


def printList():
  print()
  for item in todoList:
    print(item)
  print()


while True:
  menu = input("view, add, or edit their list?:")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What do you want to add to the list?: ")
    if item not in todoList:
      todoList.append(item)
  elif menu == "edit":
    removal = input("Do you want to remove everything from the list?")
    if removal == "yes":
      todoList = []
    else:
      item = input("Which item has you completed? ")
      if item in todoList:
        confirm = input(f"Are you sure you want to remove {item}? ")
        if confirm == "yes":
          todoList.remove(item)
      else:
        print(f"{item} was not in the list")

  printList()
