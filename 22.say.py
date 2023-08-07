import sys
# from sayings import goodbye
# from sayings import hello     #this will read sayings module from top to bottom, 
                                #left to right and import specifically hello function but 
                                #unfortunately when it reads the last line of the file to call 
                                #main() therefore main gets called.

import sayings_21

if len(sys.argv) == 2:
    # hello(sys.argv[1])
    # goodbye(sys.argv[1])
    sayings_21.hello(sys.argv[1])
    sayings_21.goodbye(sys.argv[1])
