import sys 

def main():
    
    input_validation()

    lien = count_lines(sys.argv[1])
    print(lien)

def input_validation():

    if len(sys.argv) > 2:
        print("to many command-line argument ")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("to few command-line argument ")
        sys.exit(1)

    if ".py" not in sys.argv[1]:
        print("not a python file")
        sys.exit(1)

def count_lines(File):

    try :
        with open(File ,'r') as f:
            f_lines = f.readlines()
    except FileNotFoundError:
        print("File Not Found")
        sys.exit(1)

    line_counter = 0
    for line in f_lines :
        if line.strip().startswith("#"):
            pass
        elif line.strip().startswith('"""'):
            pass  
        elif line.strip() == "":
            pass
        else:
            line_counter += 1
        
    return line_counter

if __name__ == "__main__":
    main()