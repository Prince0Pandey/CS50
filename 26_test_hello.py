from hello_25 import hello

# def test_hello():
#     hello("Prince") == "hello, Prince"      #this will give error as hello("Prince") is not returning anything but
#                                             #printing "hello, Prince" so how do we can use it to compare.
#     hello() == "hello, world"

'''here we separately testing because we want our test more traceable'''
def test_default():
    hello() == "hello, world"

def test_argument():
    for name in ["vicky","ratnesh","mukesh"]:
        hello(name) == f"hello, {name}"

    hello("Prince") == "hello, Prince"