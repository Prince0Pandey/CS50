'''
i = 3
while i != 0:
    print("meow")
    i-=1
'''

'''
i = 0
while i < 3:
    print("meow")
    i+=1
'''

'''
for i in [3,3,3,'bjbdb',"f"]:
    print("meow")
'''

'''
for i in range(3):
    print("meow")
'''

'''
for _ in range(3):              # same as above code
    print("meow")
'''

# print("meow\n" * 3,end = "")

while True:
    n = int(input("what's n?"))
    if n > 0:
        break           # NOTE: break is in 'if' but it will break any fresh loop irrespective of where it is placed

for _ in range(n):
    print("meow")