import sys

def downcase_all(s: str) -> str:
    return s.lower()

if len(sys.argv) <= 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_all(arg))