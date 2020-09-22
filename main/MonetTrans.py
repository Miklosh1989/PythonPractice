from Meth import main

from bankOperation import addOperation, addAccount


class Bank:
    name = "БПС-Сбербанк"
    def operation(self):
        main(int(input("Введите сумму в рублях: ")), int(input("Введите сумму в копейках: ")))
person = Bank()
# person.operation() Task1

print(addOperation(int(input("Введите сумму вклада: ")), int(input("На сколько лет: "))))

sum = addAccount(input())
print(sum)
sum = addAccount(input())
print(sum)







