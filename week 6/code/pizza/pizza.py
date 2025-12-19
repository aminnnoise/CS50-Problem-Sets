import tabulate
import sys
import csv


def main():
    validation()
    read(sys.argv[1])

def validation():
    if len(sys.argv) > 2:
        sys.exit("to many command-line argument ")
    elif len(sys.argv) < 2:
        sys.exit("to few command-line argument ")
    
    if '.csv' not in sys.argv[1]:
        sys.exit("Not a CSV file")



def read(fileinput):
    body = []
    header = []
    try:
        with open(fileinput) as file :
            reader = csv.reader(file)
            for index , value in enumerate(reader):
                if index == 0 :
                    header.append(value)
                    continue
                body.append(value)
        print(tabulate.tabulate(body , *header , tablefmt="grid"))
    
    except FileNotFoundError:
        sys.exit("File Not Found")


if __name__ == "__main__":
    main()