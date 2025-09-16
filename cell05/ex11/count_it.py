import sys

if len(sys.argv) <= 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    params = sys.argv[1:]
    for p in params:
        print(f"{p}: {len(p)}")