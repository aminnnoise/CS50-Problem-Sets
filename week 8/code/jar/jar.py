class Jar:
    def __init__(self, capacity: int = 12):
        if not type(capacity) == int :
            raise ValueError("Capacity must be non-negative.")
        if capacity < 0:
            raise ValueError("Capacity must be non-negative.")
        self.__capacity = capacity
        self.__size = 0

    def deposit(self, n: int):
        if self.__size + n > self.__capacity:
            raise ValueError("Not enough space in the jar.")
        self.__size += n

    def withdraw(self, n: int):
        if n > self.__size:
            raise ValueError("Not enough cookies to withdraw.")
        self.__size -= n

    def __str__(self):
        return "🍪" * self.__size

    def __repr__(self):
        return f"Jar(capacity={self.__capacity}, size={self.__size})"

    @property
    def capacity(self):
        return self.__capacity

    @property
    def size(self):
        return self.__size

