names = []

for i in range(10):
    name = input("Enter name: ")
    names.append(name)

print(names)

for i in range(10):
  print(names.pop(0))
