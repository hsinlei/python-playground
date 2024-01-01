import os, time

listOfEmail = []


def prettyPrint():
  os.system("clear")
  print("listOfEmail")
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter += 1
  time.sleep(1)


def spamEmail():

  all_email = len(listOfEmail)
  if all_email >= 10:
    for i in range(10):
      print(
        f"Dear {listOfEmail[i]}\n It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway."
      )
  else:
    for i in range(all_email):
      print(
        f"Dear {listOfEmail[i]}\n It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway."
      )


while True:
  print("Spammer Inc")
  menu = input(
    "1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("email > ")
    listOfEmail.append(email)
  elif menu == "2":
    order = input("delete email> ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spamEmail()
  time.sleep(5)
  os.system("clear")
