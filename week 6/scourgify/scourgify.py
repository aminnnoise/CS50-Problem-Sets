import sys
import csv


file_headers = ["first", "last", "house"]


def check_command_line():
    if len(sys.argv) > 3:
        sys.exit("to many")

    if len(sys.argv) < 3:
        sys.exit("to Few")


def nomalize_data(oldfile):
    db = []
    reader = csv.DictReader(oldfile)

    for each in reader:
        temp = {}
        temp["last"], temp["first"] = each["name"].split(",")

        temp["first"] = temp["first"].strip()
        temp["last"] = temp["last"].strip()

        temp["house"] = each["house"]
        db.append(temp)
    return db


def cr_csv(data, filename):
    with open(filename, "w", encoding="UTF8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=file_headers)
        writer.writeheader()
        writer.writerows(data)

def main():
    check_command_line()
    try:
        file = open(sys.argv[1], "r", encoding="utf-8")
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} not found")

    data = nomalize_data(file)

    cr_csv(data, sys.argv[2])


    file.close()


if __name__ == "__main__":
    main()