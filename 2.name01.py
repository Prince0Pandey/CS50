# ask user for there name
name = input("what's your name ? ")

'''below functions are just used once i.e it is not modified permanently'''

print("1",name.rstrip())                                #removes whitespace from right side of the str

print("2",name.lstrip())                                #removes whitespace from left side of the str

print("3",name.strip())                                 #removes whitespace from both side of the str

print("4",name.capitalize())                            #capitalize only first letter i.e value at index[0]

print("5",name.title())                                 #capitalize all the first letters of the word in a sentence

print("6",name.upper())                                 #capitalize all the letters of the str

print("7",name.lower())                                 #lower all the letters of the str

print(f"8 hello,{name.title()}")                        #format str

'''we can also add all functionality at once i.e demonstrated below'''
print(f"9 hello, {name.strip().title()}")