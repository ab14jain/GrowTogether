# class Student:
#     def __init__(self):
#         self.age = 0
#         self.name = ""

#     def display(self):
#         print("My name is", self.name + ". I am", self.age, "years old")

#     def say_hello(self, name):
#         print(self.name, "says hello to", name)

# # Main Code
# s1 = Student()
# s1.age = 10
# s1.name = "A"
# s1.display()

# s2 = s1
# s2.age = 20
# s2.name = "B"

# s2.display()
# s1.display()

# class Student:
#     def __init__(self):
#         self.age = 0
#         self.name = ""

#     def display(self):
#         print("My name is", self.name + ". I am", self.age, "years old")

#     def say_hello(self, name):
#         print(self.name, "says hello to", name)

# # Main code
# s1 = Student()
# s1.age = 10
# s1.name = "A"

# s2 = Student()

# temp = s1
# s1 = s2
# s2 = temp

# s2.display()

# class Student:
#     def __init__(self):
#         self.age = 0
#         self.name = ""

#     def display(self):
#         print("My name is", self.name + ". I am", self.age, "years old")

#     def say_hello(self, name):
#         print(self.name, "says hello to", name)

# # Main code
# if __name__ == "__main__":
#     s1 = Student()
#     s1.age = 10
#     s1.name = "A"

#     s2 = Student()

#     # Swapping ages
#     temp_age = s1.age
#     s1.age = s2.age
#     s2.age = temp_age

#     s1.display()
#     s2.display()

# class Student:
#     def __init__(self):
#         self.age = 0
#         self.name = None

#     def display(self):
#         print("My name is", self.name + ". I am", self.age, "years old")


# # Main code
# s1 = Student()
# s1.age = 10

# s2 = s1

# s2.display()


# class Student:
#     def __init__(self):
#         self.age = 0
#         self.name = ""

#     def display(self):
#         print("My name is", self.name + ". I am", str(self.age), "years old")

#     def sayHello(self, name):
#         print(self.name, "says hello to", name)

# def swap(s1, s2):
#     tage = s1.age
#     s1.age = s2.age
#     s2.age = tage

#     tname = s1.name
#     s1.name = s2.name
#     s2.name = tname

# if __name__ == "__main__":
#     s1 = Student()
#     s1.age = 10
#     s1.name = "A"

#     s2 = Student()
#     s2.age = 20
#     s2.name = "B"

#     swap(s1, s2)

#     s1.display()
#     s2.display()

class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def display(self):
        print(f"My name is {self.name}. I am {self.age} years old")

    def say_hello(self, name):
        print(f"{self.name} says hello to {name}")

def swap(s1, s2):
    temp = s1
    s1 = s2
    s2 = temp

# Main Code
s1 = Student(10, "A")
s2 = Student(20, "B")

swap(s1, s2)

s1.display()