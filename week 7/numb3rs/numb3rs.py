import re

def main():
    print(validate(input("IPv4 address: ")))

def validate(ip):
    pattern = "^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    search = re.search(pattern , ip)
    if not search:
        return False
    else:
        return True

if __name__ == "__main__":
    main()