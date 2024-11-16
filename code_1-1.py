def compute_x(a, b):
    if a > b:
        return a * a - b
    elif a == b:
        return -a
    else:  #a < b
        if b != 0:  #перевірка, щоб уникнути ділення на нуль.
            return (a * b - 1) / b
        else:
            return "Ділення на нуль неможливе"

#введення значень a та b з перевіркою.
a = int(input("Введіть a (від 1 до 100): "))
while a < 1 or a > 100:
    a = int(input("Будь ласка, введіть a ще раз (від 1 до 100): "))

b = int(input("Введіть b (від 1 до 100): "))
while b < 1 or b > 100:
    b = int(input("Будь ласка, введіть b ще раз (від 1 до 100): "))

#обчислення значення X.
X = compute_x(a, b)
print("Результат обчислення X: ", X)