# ask user for there name
name = input("what's your name ? ").strip().title()         #we can use multiple functions all at once

# say hello to user
print(f"hello, {name}")

#split user's name into first name and last name
first, last = name.split()

# say hello to user
print(f"hello, {first}")