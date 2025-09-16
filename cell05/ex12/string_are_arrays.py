import sys

i = 0

if len(sys.argv) <= 1:
    print("none")
else:
    text = sys.argv[1]
    for c in text:
        if c == 'z':
            i += 1

    if i == 0:
        print("none")
    else:
        print("z" * i)
