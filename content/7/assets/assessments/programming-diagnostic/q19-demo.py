password = input("Введіть пароль: ")
length = len(password)

if length >= 12:
    print("Пароль надійний ✅")
elif length >= 8:
    print("Пароль прийнятний, але краще зробити довше")
else:
    print("Пароль занадто короткий ❌")
