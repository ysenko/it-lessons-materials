password = "secret123"
attempts = 3

while attempts > 0:
    entered = input("Введіть пароль: ")
    if entered == password:
        print("Доступ дозволено!")
        break
    else:
        attempts = attempts - 1
        print(f"Невірний пароль. Залишилось спроб: {attempts}")

if attempts == 0:
    print("Доступ заблоковано.")
