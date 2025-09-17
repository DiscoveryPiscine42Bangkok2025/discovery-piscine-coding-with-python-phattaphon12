import sys

def MoreThanEight(s):
    print(s[:8])

def ShorterThanEight(s):
    print(s + "Z" * (8 - len(s)))

if len(sys.argv) <= 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            MoreThanEight(arg)
        elif len(arg) < 8:
            ShorterThanEight(arg)
        else:
            print(arg)