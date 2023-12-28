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
    todoList.append(item)
  elif menu == "edit":
    item = input("Which item has you completed? ")
    if item in todoList:
      todoList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
