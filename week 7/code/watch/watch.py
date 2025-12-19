import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    src_link = re.search(r"^<iframe(?:.+)? src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/(\w+)\".?(?:.+)?></iframe>$" , s)
    if src_link:
        return f"https://youtu.be/{src_link.group(1)}"
    return None

if __name__ == "__main__":
    main()
