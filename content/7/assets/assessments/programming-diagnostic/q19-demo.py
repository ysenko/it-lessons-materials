password = input("Введіть пароль: ")
length = len(password)

if length >= 8:
    print("Пароль надійний ✅")
elif length >= 6:
    print("Пароль прийнятний, але краще зробити довше")
else:
    print("Пароль занадто короткий ❌")
