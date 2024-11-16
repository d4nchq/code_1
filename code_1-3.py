def draw_pattern(N, symbol):
   #верхня частина трикутника.
   for i in range(1, N + 1):
       #виведення пробілів.
       for j in range(N - i):
           print("  ", end="")
       #виведення символів.
       for k in range(1, i + 1):
           if symbol == '1':  #якщо вибрані цифри.
               print(k, end=" ")
           else:  #якщо вибраний користувацький символ.
               print(symbol, end=" ")
       print()
   
   #нижня частина трикутника.
   for i in range(N, 0, -1):
       #спочатку виводимо відступи.
       for j in range(N - 1):
           print("  ", end="")
       #виведення символів у зворотньому порядку.
       for j in range(i, 0, -1):
           if symbol == '1':  #якщо вибрані цифри.
               print(j, end=" ")
           else:  #якщо вибраний користувацький символ.
               print(symbol, end=" ")
       print()

#отримуємо введення від користувача.
N = int(input("Введіть число N (від 2 до 8): "))

if 1 < N < 9:
   print("\nВиберіть тип символів:")
   print("1 - Цифри")
   print("або введіть будь-який символ для візерунку")
   symbol_choice = input("Ваш вибір: ")
   
   draw_pattern(N, symbol_choice)
else:
   print("Помилка! Число повинно бути більше 1 та менше 9")