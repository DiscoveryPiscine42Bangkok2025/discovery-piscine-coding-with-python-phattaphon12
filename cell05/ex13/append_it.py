import sys

if len(sys.argv) <= 1:
    print("none")
else:
    for c in sys.argv[1:]:
        if not c.endswith("ism"):
            print(c + "ism")