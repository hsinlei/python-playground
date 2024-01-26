import random, time, os

random_ideas = ["Baba", "lala", "dududu"]

while True:
  user_input = input("Add an idea or load random ideas? \n a/r. > ").strip()

  if user_input == "a":
    new_idea = input("Input your idea > ")
    input_file = open("my.ideas", "a+")
    input_file.write(f"{new_idea}\n")
    input_file.close()
    print("Nice! Your idea has been stored.")
  else:
    random_idea = random.choice(random_ideas)
    print(random_idea)
    time.sleep(4)
