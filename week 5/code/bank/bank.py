def main():
    user = input("Greeting: ")
    answer = value(user)
    print(f"${answer}")

def value(str_in):
    if (str_in.lower().startswith("hello")):
        return 0
    elif(str_in[0].lower() == 'h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()