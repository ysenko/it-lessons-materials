---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 59
style: |
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  .grid-item {
    border: 1px solid #eee;
    padding: 15px;
    border-radius: 5px;
    background-color: #fafafa;
  }
  .text-left {
    text-align: left;
    padding: 5px;
  }
  .image-center {
    max-width: 100%;
    height: auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .text-large {
    font-size: 40px;
  }
  .text-medium {
    font-size: 30px;
  }
  .text-medium-small {
    font-size: 25px;
  }
  .text-small {
    font-size: 18px;
  }
  .text-tiny {
    font-size: 14px;
  }
  .card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    background-color: #f9f9f9;
  }
  .important-to-remember {
    background-color: #fff3cd;
    border-left: 6px solid #ffecb5;
    padding: 15px;
    margin: 15px 0;
  }
  .borderless {
    border: 0px;
  }
  .task {
    background-color: #e3f2fd;
    border-left: 5px solid #2196f3;
    padding: 15px;
    border-radius: 8px;
  }
  .emoji-large {
    font-size: 3em;
    text-align: center;
    display: block;
  }

---

# 🔁 Цикл `while` в Python

## 🏫 Урок **59**

---

## 🎯 Сьогодні ми дізнаємося

- 🔁 Що таке **цикл** і навіщо він потрібен.
- 📌 Дві форми: **`while`** та **`while...else`**.
- ♾️ Що таке **нескінченний цикл** і як його зупинити.
- ⌨️ Як **самостійно писати** програми з циклами.

---

## 🧠 Пригадайте!

<div class="card">

Що виведе цей код?

```python
x = 5
if x > 3:
    print("Більше")
else:
    print("Менше або рівне")
```

Навіщо потрібен відступ у тілі `if`?

Яке значення поверне `10 > 3`?

</div>

---

## 💡 Навіщо потрібен цикл?

<div class="important-to-remember text-medium-small">

Завдання: вивести числа від 1 до 5.

</div>

<div class="grid-container">
<div class="text-left text-medium-small">

**Без циклу — 5 рядків:**
```python
print(1)
print(2)
print(3)
print(4)
print(5)
```
А якщо до 1000? 😱

</div>
<div class="text-left text-medium-small">

**З циклом — 3 рядки:**
```python
count = 1
while count <= 5:
    print(count)
    count = count + 1
```
Працює для будь-якого числа! 🎉

</div>
</div>

---

## 🔁 Цикл — ключові поняття

<div class="card text-medium-small">

**Цикл** — структура управління, яка **повторює** блок інструкцій.

</div>

<div class="text-medium-small">

| Термін | Пояснення |
|---|---|
| **Умова циклу** | Вираз, що перевіряється перед кожним повторенням |
| **Тіло циклу** | Блок коду, що виконується при кожному повторенні |
| **Ітерація** | Одне виконання тіла циклу |

</div>

<div class="important-to-remember text-medium-small">

Поки умова **`True`** → тіло виконується. Як тільки **`False`** → цикл зупиняється.

</div>

---

## 🔁 Синтаксис `while`

<div class="important-to-remember">

```python
while умова:
    # тіло циклу
    # (виконується, поки умова True)
```

</div>

<div class="text-medium-small">

- Після `while` — обов'язкова **двокрапка `:`**
- Тіло — з **відступом** (4 пробіли або Tab)
- Умова перевіряється **перед кожною ітерацією**
- Якщо умова відразу `False` — тіло **не виконується жодного разу**

</div>

---

## 🔁 Приклад: лічильник від 1 до 5

<div class="grid-container">
<div class="text-left text-medium-small">

```python
count = 1
while count <= 5:
    print(count)
    count = count + 1
print("Готово!")
```

</div>
<div class="text-left text-small">

**Покроковий розбір:**

| `count` | Умова `count <= 5` | Дія |
|---|---|---|
| 1 | `True` | виводить `1` |
| 2 | `True` | виводить `2` |
| 3 | `True` | виводить `3` |
| 4 | `True` | виводить `4` |
| 5 | `True` | виводить `5` |
| 6 | `False` | цикл зупиняється |

**Вивід:**
```
1
2
3
4
5
Готово!
```

</div>
</div>

---

## 🔁 Приклад: «Вгадай число»

<div class="card text-medium-small">

```python
secret = 7
guess = int(input("Вгадай число від 1 до 10: "))
while guess != secret:
    print("Не вгадав! Спробуй ще раз.")
    guess = int(input("Вгадай число від 1 до 10: "))
print("Правильно! Це число", secret)
```

</div>

<div class="important-to-remember text-medium-small">

Цикл виконується **невідому кількість разів** — доки гравець не вгадає число.
Саме тут `while` зручніший за інші цикли!

</div>

---

## ♾️ Нескінченний цикл

<div class="grid-container">
<div class="text-left text-medium-small">

**Небезпека! ⚠️**
```python
x = 1
while x > 0:
    print(x)
    # x не змінюється!
    # умова завжди True
```

Цикл ніколи не зупиниться!

</div>
<div class="text-left text-medium-small">

**Як зупинити в Thonny:**

🟥 Кнопка **Stop**
або
⌨️ **Ctrl + C**

**Правило:**
Завжди перевіряйте, чи може умова стати `False`!

</div>
</div>

---

## ♾️ Оператор `break`

<div class="important-to-remember text-medium-small">

**`break`** — негайно виходить з циклу, ігноруючи умову.

</div>

<div class="card text-medium-small">

```python
while True:
    answer = input("Введіть 'стоп' для виходу: ")
    if answer == "стоп":
        break
    print("Ви ввели:", answer)
print("Програма завершена.")
```

</div>

<div class="text-medium-small">

`while True:` — цикл, що завжди повторюється. Програмний вихід з нього — через **`break`** або виняток.

</div>

---

## 🔁 Форма `while...else`

<div class="important-to-remember">

```python
while умова:
    # тіло циклу
else:
    # виконується ОДИН РАЗ
    # після природного завершення циклу
```

</div>

<div class="card text-medium-small">

⚡ Ключова відмінність:
- Якщо цикл завершився **природно** (умова стала `False`) → `else` **виконується**.
- Якщо цикл зупинився через **`break`** → `else` **НЕ виконується**.

</div>

---

## 🔁 `while...else` — базовий приклад

<div class="grid-container">
<div class="text-left text-medium-small">

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1
else:
    print("Цикл завершено!")
```

**Вивід:**
```
1
2
3
Цикл завершено!
```

</div>
<div class="text-left text-medium-small">

Умова `count <= 3` стала `False` (count = 4) → цикл завершився **природно** → `else` виконався.

</div>
</div>

---

## 🔁 `while...else` — три спроби входу

<div class="text-medium-small">

```python
password = "python123"
attempts = 3
while attempts > 0:
    entered = input("Введіть пароль: ")
    if entered == password:
        print("Вхід виконано! ✅")
        break
    attempts = attempts - 1
    print(f"Неправильно. Залишилось спроб: {attempts}")
else:
    print("Обліковий запис заблоковано. 🔒")
```

</div>

<div class="important-to-remember text-medium-small">

✅ Пароль вірний → `break` → `else` **не виконується**.
❌ Спроби вичерпано → умова `False` → `else` **виконується**.

</div>

---

## ⚠️ Типові помилки

<div class="text-medium-small">

| Помилка | Симптом | Виправлення |
|---|---|---|
| Немає оновлення лічильника | Нескінченний цикл | Додати `count = count + 1` |
| Немає `:` після `while` | `SyntaxError` | Додати `:` |
| Немає відступу в тілі | `IndentationError` | 4 пробіли або Tab |
| Умова завжди `True` | Нескінченний цикл | Перевірити логіку умови |

</div>

<div class="card text-medium-small">

```python
# ❌ Нескінченний цикл — лічильник не оновлюється:
count = 1
while count <= 5:
    print(count)   # count ніколи не стає > 5!

# ✅ Правильно:
count = 1
while count <= 5:
    print(count)
    count = count + 1
```

</div>

---

## ⌨️ Практична робота — Завдання 1

<section class="task text-medium-small">

## 🔢 Завдання 1 — Сума від 1 до N

Напиши програму, яка:
1. Запитує натуральне число: `n = int(input("Введіть N: "))`.
2. Використовуючи `while`, обчислює суму від 1 до N включно.
3. Виводить результат.

**Приклад виводу:**
```
Введіть N: 5
Сума від 1 до 5 = 15
```

**Підказка:** заведи змінну `total = 0` і додавай до неї `count` на кожній ітерації.

</section>

---

## ⌨️ Практична робота — Завдання 2

<section class="task text-medium-small">

## 🔐 Завдання 2 — Перевірка пароля

Напиши програму з `while...else`:

1. Пароль `"qwerty"` задано у коді.
2. Програма дає **3 спроби** ввести правильний пароль.
3. Якщо вірний → вивести **«Доступ дозволено»** і завершити цикл.
4. Якщо всі спроби вичерпано → вивести **«Доступ заблоковано»**.

</section>

---

## ⌨️ Практична робота — Завдання 3 ⭐

<section class="task text-medium-small">

## 🎲 Завдання 3 ⭐ — Вгадай число

Напиши програму:
1. `import random` та згенерувати `random.randint(1, 20)`.
2. Гравець вводить числа, поки не вгадає.
3. Після кожної спроби — підказка **«Більше»** або **«Менше»**.
4. Після вгадування вивести **кількість спроб**.

</section>

---

## 🤔 Підсумок уроку

<div class="text-medium-small">

- 🔁 **`while умова:`** — повторює тіло, поки умова `True`.
- 🛑 **`break`** — негайний вихід з циклу.
- 🔁 **`while...else`** — `else` виконується після **природного** завершення циклу (але не після `break`).
- ♾️ **Нескінченний цикл** — умова ніколи не стає `False`. Зупинити: **Stop** або **Ctrl+C**.
- ⚠️ Обов'язково оновлювати лічильник всередині циклу!

</div>

---

## 🏠 Домашнє завдання

<section class="task text-medium-small">

📖 **Опрацювати підручник** (розділ про цикл `while`).

Виконати у 👉 [**onlineide.pro/playground/python**](https://www.onlineide.pro/playground/python)

**Програма «Зворотний відлік»:**
1. Запитати число N: `n = int(input("Введіть N: "))`.
2. Вивести числа від N до 1 (по одному в рядку).
3. Після відліку вивести **«Старт! 🚀»**.

**За бажанням ⭐ — «Таблиця множення»:**
- Запитати число від 1 до 9, вивести таблицю множення (×1 до ×10) за допомогою `while`.

</section>
