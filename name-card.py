people_name = []

def print_people_name():
  for i in range(1, len(people_name) + 1):
    print(f"{i}: {people_name[i-1]}")

while True:
  first_name = input("What is your first name?").strip().capitalize()
  last_name = input("What is your last name?").strip().capitalize()

  full_name = f"{first_name} {last_name}"

  if full_name not in people_name:
    people_name.append(full_name)
    print_people_name()
