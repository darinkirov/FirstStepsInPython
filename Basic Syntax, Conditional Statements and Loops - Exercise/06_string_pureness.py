def is_pure_string(s):
    forbidden_chars = {',', '.', '_'}
    for char in s:
        if char in forbidden_chars:
            return False
    return True

def main():
    n = int(input("Enter the number of strings: "))
    for _ in range(n):
        string = input("Enter a string: ")
        if is_pure_string(string):
            print(f"{string} is pure. ")
        else:
            print(f"{string} is not pure!")

if __name__ == "__main__":
    main()
