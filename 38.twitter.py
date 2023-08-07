import re

url = input("twitter URL: ").strip()

#waste,username = url.split(".com/")
#username = url.replace("https://twitter.com/","")
#username = url.removeprefix("https://twitter.com/PrinceP344471")

'''
re.sub(pattern, repl, string, count, flags=0)     syntax
re.split(pattern, string, maxsplit = 0, flags = 0)
re.findall(pattern, string, flags = 0)
'''

# username = re.sub("^(https?://)?(www\.)?twitter\.com/","",url)
# print(f"username: {username}")

matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_])$", url, re.IGNORECASE)
if matches:
    print(f"username: {matches.group(1)}")