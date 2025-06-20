class P:
    def __init__(self):
        self.d1 = 10
        self.d = 100

    def fun1(self):
        print("P's fun1")

    def fun(self):
        print("P's fun")

    def sfun():
        print("P's sfun")


class C(P):
    def __init__(self):
        super().__init__()
        self.d2 = 20
        self.d = 200

    def fun2(self):
        print("C's fun2")

    def fun(self):
        print("C's fun")

    def sfun():
        print("C's sfun")


# Main code
obj = C()
print(obj.d1)
print(obj.d)
obj.fun1()
obj.fun()
C.sfun()