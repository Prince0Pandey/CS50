# email = input("what's your email? ").strip()

# # if "@" and "." in email:
# if "@" in email and "." in email:
#     print("valid email")

# else:
#     print("invalid email")


# email = input("what's your email? ").strip()

# username, domain = email.split("@")

# if (username) and ("." in domain):    #if username contain character then return true & "." in domain
#     print("valid email")

# else:
#     print("invalid email")


#validator for .edu mails

# email = input("what's your email? ").strip()
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("valid email")

# else:
#     print("invalid email")


'''
.       any number of charater except a newline
*       0 or more repetitions 
+       1 or more repetitions
?       0 or 1 repetitions
{m}     m repetitions
{m,n}   m-n repetitions

^       matches the start of the string
$       matches the end of the string and just before the newline at th eend of the string

[]      set of characters
[^]     complementing the set

\d      decimal digit
\D      not a decimal digit
\s      whitespace character
\S      not a whitespace character
\w      word character...as well as numbers and underscore i.e [a-zA-Z0-9_]
\W      not a word character...as well as numbers and underscore i.e [a-zA-Z0-9_]

A|B     either A or B
(...)   a group
(?:...) non-capturing version

{re.IGNORECASE   re.MULTILINE    re.DOTALL} this three are used inside a re.search function as flags
re.search()
re.match()      don't need to specify carat symbol at the beginning
re.fullmatch()  don't need to specify carat symbol at the beginning and dollar symbol at the end
'''

import re

email = input("what's your email? ").strip() #here we can use .lower() to convert user input into 
# lower case because email address's are not case sensitive(we havn't include .EDU or .COM i.e
# upper case) if we don't add flags

# if re.search(r"^[^@][^ ]+@[^@][^ ]+\.edu$",email):    #r => raw string    
#backslash helps to add any new pattern because without backslash re.search function will think . after slash as any character(ex. ?edu or vardedu)
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|org|gov|edu.in)$",email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
    
# input:    malan@cs50.harvard.edu
# input:    malan@harvard.edu
# (\w+\.)?  (a to z, 0-9,underscore) 0 or 1 repetitions (example: cs50.)
# if we want more than 1 sub domain name than use *
    

'''
#for valid email address that some browser's use now a days but not gmail

import re
email = input("what's your email? ").strip()
if re.search(r"^[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
'''