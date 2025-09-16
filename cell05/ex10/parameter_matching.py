import sys

if len(sys.argv) < 2:
    print("none")
else:
    text = input("What was the parameter? ")
    keyword = sys.argv[1]
    if (text == keyword):
        print("Good job!")
    else:
        print("Nope, sorry...")