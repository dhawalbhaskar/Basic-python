class MyClass:
    def __init__(self):
        self._protected_data = "This is protected"
        self.__private_data = "This is private"

obj = MyClass()
print(obj._protected_data)
print(obj._MyClass__private_data)
