#pytest allow us to run a folder for test but for that we have to create '__init__.py' file then python tells to
#treat that folder not just a module but as a package

from hello_25 import hello

def test_default():
    hello() == "hello, world"

def test_argument():
    hello("Prince") == "hello, Prince"