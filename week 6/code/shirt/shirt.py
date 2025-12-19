import sys
from PIL import Image, ImageOps

allowed_ext = ["png", "jpg", "jpeg"]

def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("TOO Few command-line argument")
    if len(sys.argv) > 3:
        sys.exit("TOO Many command-line argument")

def check_arg_extension():
    input_ext = sys.argv[1].rsplit(".")[-1]
    output_ext = sys.argv[2].rsplit(".")[-1]
    
    if output_ext.lower() not in allowed_ext:
        sys.exit(f"{output_ext} is not allowed")
    
    if input_ext.lower() not in allowed_ext:
        sys.exit(f"{input_ext} is not allowed")
    
    if input_ext.lower() != output_ext.lower():
        sys.exit("diffrent extenstion input and output") 

def main():
    check_command_line()
    
    check_arg_extension()

    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt can not open !")

    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Shirt can not open !")

    size = shirt.size

    muppet = ImageOps.fit(muppet, size)

    muppet.paste(shirt, shirt)

    muppet.save(sys.argv[2])

if __name__ == '__main__':
    main()
