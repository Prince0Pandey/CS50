import re
 
name = input("what's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$",name)       # matches will store value that are in parenthesis
# there are 2 parenthesis so matches will store 2 value
if matches:
    # last, first = matches.groups()
    # name = f"{first} {last}"
    
    # last = matches.group(1)                     # this will give me first parenthesis value
    # first = matches.group(2)                    # this will give me second parenthesis value
    # name = f"{first} {last}"
    
    name = matches.group(2) + " " + matches.group(1)
print("hello,", name)

# same as above but directly checking using if condition

import re
name = input("what's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$",name):
# := is a operator that not only checks for boolean expression but if true stores the value 
# to left side variable
    name = matches.group(2) + " " + matches.group(1) 
print("hello,", name)