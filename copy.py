from shutil import copyfile
from sys import argv
def main() -> None:
    if len(argv)-1:
        print(len(argv))
        copyfile("template.py", f"day{argv[1]}.py")

if __name__ == "__main__":
    main()