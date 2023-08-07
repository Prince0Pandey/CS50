# def main():
#     yell("This", "is", "CS50","course")

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)
    
# if __name__ == "__main__":
#     main()


# def main():
#     yell("This", "is", "CS50","course")

# def yell(*words):
#     uppercased = map(str.upper, words)
#     # map(function, iterable,...):map will apply given function to all the arguments stored in
#     # words and return it to uppercased
#     print(*uppercased)
    
# if __name__ == "__main__":
#     main()


def main():
    yell("This", "is", "CS50","course")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    
if __name__ == "__main__":
    main()