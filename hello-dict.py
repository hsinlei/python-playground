moke_beast = {}


def prettyPrint():
  print()

  for key, value in moke_beast.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()


while True:
  name = input("Input your beast's name >  ").strip().title()
  moke_beast_details = {
    "type": None,
    "special move": None,
    "starting HP": None,
    "starting MP": None
  }
  moke_beast_details["type"] = input(
    "Input your beast's type >  ").strip().title()
  moke_beast_details["special move"] = input(
    "Input your beast's special move >  ").strip().title()
  moke_beast_details["starting HP"] = input(
    "Input your beast's starting HP >  ").strip().title()
  moke_beast_details["starting MP"] = input(
    "Input your beast's starting MP >  ").strip().title()

  moke_beast[name] = moke_beast_details
  prettyPrint()
  again = input("Again? y/n > ").strip().lower()
  if again == "n":
    break
