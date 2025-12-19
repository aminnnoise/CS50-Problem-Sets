import string

def main():
    txt = input()
    print(shorten(txt))

def shorten(txt):
    for i in txt:
        if i in string.punctuation:
            txt = txt.replace(i,"")
        if i.upper() in ['A', 'E', 'I', 'O', 'U']:
            txt = txt.replace(i,"")
    return txt

if __name__ == "__main__":
    main()