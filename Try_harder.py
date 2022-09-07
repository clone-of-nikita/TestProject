class Calculator:
    def __init__(self,x):
        self.x = x
        self.calculating()

    def calculating(self,a,b):
        x = input("What u whant to do: ")
        if x == "+":
            print(a + b," sum of two element`s")
        elif x == "-":
            print(a - b, "minus dvuh elementov")
        elif x == "/":
            print(a/b, "delenie dvuh elementov")
        elif x == "*":
            print(a*b,"umnozshenie dvuh elementov")
        else:
            pass


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    Calculator.calculating(0,a,b)