class First:
    def __init__(self, value: str):
        self.value = value

    def print_first(self, name: str):
        print(f"first name is: {self.value} - {name}")

class Second(First):
    def __init__(self, first_name: str, second_name: str):
        super().__init__(first_name)
        self.second_name = second_name
        self.first_name = first_name

    def print_second(self, name: str):
        print(f"second name is: {self.first_name} - {self.second_name} - {name}")

class Third(Second):
    def __init__(self, first_name, second_name, third_name: str):
        super().__init__(first_name, second_name)
        self.third_name = third_name

    def print_third(self, name: str):
        print(f"third name is: {self.value} - {name}")
        print("Звернувся, використовуючи super(), до методу класа Second, який є батьком класу Third")
        super().print_second(name)
        print("Звернувся, використовуючи super(), до методу класа First, який є дідом класу Third")
        super().print_first(name)

class Five:
    def __init__(self, number: int):
        self.number = number

class Fourth(First, Five):
    def __init__(self, first_name, number, fourth_name: str):
        super().__init__(first_name)
        self.first_name = first_name
        self.number = number
        self.fourth_name = fourth_name

    def print_fourth(self, name: str):
        print(f"fourth name is: {self.fourth_name} - {self.number} - {self.first_name} - {name}")

first_object = First("first")
second_object = Second("bingo", "second")
third_object = Third("Hello", "world", "third")
fourth_object = Fourth("world", 100 , "fourth")
print("Звернувся до методу класа First")
first_object.print_first("first-first")
print("Звернувся до методу класа Second")
second_object.print_second("second-second")
print("Звернувся до методу класа First, який є батьком класу Second")
second_object.print_first("second-first")
print("Звернувся до методу класа Third")
third_object.print_third("third-third")
print("Звернувся до методу класа Second, який є батьком класу Third")
third_object.print_second("third-second")
print("Звернувся до методу класа First, який є дідом класу Third")
third_object.print_first("third-first")
print("Звернувся до методу класа First, який є батьком класу Fourth")
fourth_object.print_first("fourth-first")
print("Звернувся до власного методу класа Fourth")
fourth_object.print_fourth("Petro")