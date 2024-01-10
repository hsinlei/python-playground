todo = []


def prettyPrint(list, prio):
  count = 0
  for row in list:
    print(f"\n{count} : ")
    for item in row:
      if prio == "all":
        print(f"{item:^10}", end=' | ')
      elif prio == row[2]:
        print(f"{item:^10}", end=' | ')
    count += 1


while True:
  menu = input("\nDo you want to add, view, remove, or edit a to do? > ")

  if menu.strip().lower() == "add":
    todolist = input("What is the task? > ")
    duedate = input("When is it due by? > ")
    priority = input("What is the priority? > ")
    row = [todolist, duedate, priority]
    todo.append(row)
    print("Thanks, this task has been added.")

  elif menu.strip().lower() == "view":
    view_options = input("\nDo you want to view all or view priority?")
    if view_options.strip().lower() == "all":
      prettyPrint(todo, "all")
    else:
      view_prio = input("Which priority do you want to view? > ")
      choose = view_prio.strip().lower()
      prettyPrint(todo, choose)

  elif menu.strip().lower() == "edit":
    prettyPrint(todo, "all")
    a_option = int(input("Which to do do you want to edit?"))
    todolist = input("New task name > ")
    duedate = input("New due date > ")
    priority = input("New priority > ")
    todo[a_option] = [todolist, duedate, priority]
    prettyPrint(todo, "all")
  elif menu.strip().lower() == "remove":
    prettyPrint(todo, "all")
    remove_option = int(input("Which to do do you want to remove?"))
    todo.remove(todo[remove_option])
    prettyPrint(todo, "all")