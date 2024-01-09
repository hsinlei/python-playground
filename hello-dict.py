moke_beast = {
  "name": None,
  "type": None,
  "special move": None,
  "starting HP": None,
  "starting MP": None
}

for name, value in moke_beast.items():
  moke_beast[name] = input(f"Input your beast's {name} >  ").strip().title()

print(
  f"Your beast is called {moke_beast['name']}. It is an {moke_beast['type']} beast with a special move of {moke_beast['special move']}"
)
