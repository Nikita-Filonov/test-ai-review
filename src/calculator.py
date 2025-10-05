from src.utils import log_message


class Calculator:
    def __init__(self):
        self.last_result = 0

    def add(self, a, b):
        log_message(f"Adding {a} + {b}")
        return a + b

    def divide(self, a, b):
        log_message(f"Dividing {a} / {b}")
        if b == 0:
            print("Division by zero!")
            return None
        return a / b

    def power(self, base, exp):
        res = base ** exp
        log_message(f"Power: {base}^{exp}={res}")
        return res


if __name__ == "__main__":
    c = Calculator()
    print(c.add(2, 2))
    print(c.divide(10, 0))
    print(c.power(2, 8))
