"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

for word in some_words:# It will not print word 
    print(word)#not printed

for x in some_words:#it will not print
    print(x)#not printed

print(some_words)#It will not print

if len(some_words) > 3:#It checks the length of the argument(Some_words). Any characters stored within the argument that is bigger than 3 characters will be printed
    print('some_words contains more than 3 words') #'some_words contains more than 3 words') will be printed

def usefulFunction():#The command will be name the six attributes of the computer ,(retursn a namedtuple)
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())#returned system, node, release, version, machine and processor information

usefulFunction()
