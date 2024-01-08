import random

listOfWords = [
  "british", "suave", "integrity", "accent", "evil", "genius", "Downton"
]

lettersUsed = []
wordChosen = random.choice(listOfWords)
print(wordChosen)
wrongGuess = 0
print_word = [len(wordChosen) * " _ "]
print(print_word)

while True:
  userGuess = input("Type in a letter > ").strip().lower()
  lettersUsed.append(userGuess)

  if userGuess in wordChosen:
    print("Correct Guess!")
  else:
    wrongGuess += 1
    print("Wrong Guess")

  # separate printing hangman from lives
  for each_right_guess in wordChosen:
    if each_right_guess in lettersUsed:
      print(each_right_guess, end="")
    else:
      print("_", end="")

  if wrongGuess > 6:
    print("You lose! ")
    break
