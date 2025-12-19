def main():
    user_input = input("Here: ")
    user_input = convert(user_input)
    print(gauge(user_input))



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+ "%"



def convert(user):
    while True:
        try:
            one,two = user.split("/")
            one =int(one)
            two = int(two)
            if one > two or one<0 :
                continue
        except ValueError:
            raise
        else:
            try:
                result = (one / two)
                result *= 100
                result = round(result)
                result = int(result)
            except ZeroDivisionError:
                raise
            else:
                return result



if __name__ == "__main__":
    main()