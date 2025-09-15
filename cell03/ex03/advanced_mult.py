import sys

if len(sys.argv) > 1:
    print("none")
else:
    # วนรอบตั้งแต่ 0 ถึง 10
    for number in range(11):
        line = f"Table de {number}:"
        for i in range(11):
            result = number * i
            line += " " + str(result)
        print(line)