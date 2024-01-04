people_name = []


def print_people_name():
  for i in range(1, len(people_name) + 1):
    print(f"{i}: {people_name[i-1]}")


while True:
  first_name = input("What is your first name?").strip().capitalize()
  last_name = input("What is your last name?").strip().capitalize()

  slice_first = first_name[0:3]
  slice_last = last_name[0:3]
  userfirstname = slice_first + slice_last.lower()

  maiden_name = input("What is your mother's maiden name?").strip()
  city_born = input("Which city were you born?")
  slice_maiden = maiden_name[0:2]
  slice_city = city_born[-3:]
  userlastname = slice_maiden + slice_city.lower()

  full_name = f"{userfirstname} {userlastname}"

  if full_name not in people_name:
    people_name.append(full_name)
    print_people_name()
