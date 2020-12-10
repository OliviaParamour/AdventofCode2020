from sys import argv
def main() -> None:
    if len(argv)-1:
        print(len(argv))
        file = ""
        with open("template.py", "r") as f:
            file = f.read()
            file = file.replace(f"day x", f"day {argv[1]}")
            file = file.replace(f"dayx", f"day{argv[1]}")
        with open(f"day{argv[1]}.py", "w") as f:
            f.write(file)
    else:
        print("copy.py needs one parameter to create file from template.")

if __name__ == "__main__":
    main()