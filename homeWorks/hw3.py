class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self, input_balance):
        result = self._balance + input_balance
        return f"ваш баланс пополнен на {input_balance}, ваш баланс сейчас-{result}"

    def _kill(self):
        self._balance = 0
        return f"вы обнулили свой баланс!"

    def __jackpot(self):
        self._balance = self._balance * 10
        return self._balance

    def copy_balance(self, other):
        self._balance += other._balance
        return self._balance


user1 = Bank("Abdumalik", 100)
user2 = Bank("Imran", 200)

print(user1.moneyX(900))
print(user1._kill())
print(user2.copy_balance(user1))


class Calculator:

    def __add__(self, n1, n2):
        return n1 + n2

    def __sub__(self, n1, n2):
        return n1 - n2

    def __mul__(self, n1, n2):
        return n1 * n2

    def __truediv__(self, n1, n2):
        return n1 / n2



calculate = Calculator()

print(calculate.__add__(12, 56))