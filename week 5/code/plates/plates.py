def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def end_str(a):
    if a == " ":
        return True
    array = a.split()
    for each in array:
        if (each.isnumeric()):
            continue
        return False
    return True


def is_valid(plt):
    if (plt[0].isnumeric() and plt[1].isnumeric()):
        return False
    if (len(plt) > 6 or len(plt) < 2):
        return False
    tempo = ''

    for one in range(len(plt)):

        if (plt[one].isnumeric()):
            if plt[one] == '0':
                return False
            tempo = plt[one:]
            break
    if tempo != " ":
        resault = end_str(tempo)
        if resault != True:
            return False
    return True

            

    for i in plate:
        if i.isnumeric():
            if plate[-1].isalpha():
                return False
            else :
                return True

if __name__ == "__main__":
    main()