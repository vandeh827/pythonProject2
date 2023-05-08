class Maths:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y

class Physics:
    def velocity(self, x, y):
        return x / y

    def acceleration(self, x, y):
        return x / y

    def force(self, x, y):
        return x * y

    def momentum(self, x, y):
        return x * y

    def energy(self, x, y):
        return x * y

while True:
    print("Which subject do you want to calculate? (maths/physics)")
    subject = input()

    if subject == "maths":
        maths = Maths()
        print("Which operation do you want to perform? (add/subtract/multiply/divide/power)")
        operation = input()

        print("Enter the first number:")
        x = float(input())
        print("Enter the second number:")
        y = float(input())

        if operation == "add":
            result = maths.add(x, y)
        elif operation == "subtract":
            result = maths.subtract(x, y)
        elif operation == "multiply":
            result = maths.multiply(x, y)
        elif operation == "divide":
            result = maths.divide(x, y)
        elif operation == "power":
            result = maths.power(x, y)
        else:
            print("Invalid operation!")
            continue

        print("The result is:", result)
        break

    elif subject == "physics":
        physics = Physics()
        print("Which operation do you want to perform? (velocity/acceleration/force/momentum/energy)")
        operation = input()

        print("Enter the first number:")
        x = float(input())
        print("Enter the second number:")
        y = float(input())

        if operation == "velocity":
            result = physics.velocity(x, y)
        elif operation == "acceleration":
            result = physics.acceleration(x, y)
        elif operation == "force":
            result = physics.force(x, y)
        elif operation == "momentum":
            result = physics.momentum(x, y)
        elif operation == "energy":
            result = physics.energy(x, y)
        else:
            print("Invalid operation!")
            continue

        print("The result is:", result)
        break

    else:
        print("Invalid subject!")