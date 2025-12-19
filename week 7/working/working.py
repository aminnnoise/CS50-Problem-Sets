import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s.strip(), re.IGNORECASE):
        h1 = int(match.group(1))
        m1 = int(match.group(2) or 0)
        p1 = match.group(3).upper()
        h2 = int(match.group(4))
        m2 = int(match.group(5) or 0)
        p2 = match.group(6).upper()

        if p1 == "PM" and h1 != 12: h1 += 12
        if p1 == "AM" and h1 == 12: h1 = 0
        if p2 == "PM" and h2 != 12: h2 += 12
        if p2 == "AM" and h2 == 12: h2 = 0

        if max(h1, h2) > 23 or max(m1, m2) > 59:
            raise ValueError

        return f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}"

    raise ValueError("Invalid format")

if __name__ == "__main__":
    main()