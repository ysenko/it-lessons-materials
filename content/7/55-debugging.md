---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 55
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

# 🐛 Налагодження алгоритмів у середовищі програмування

## 🏫 Урок **55**

---

## 🎯 Сьогодні ми навчимося

- 🐛 Що таке **налагодження (debugging)** та звідки ця назва.
- 🔴 Розпізнавати **типи помилок** Python: `SyntaxError`, `NameError`, `TypeError`, `IndexError`, `ValueError`.
- 🔍 Читати **повідомлення про помилки** у Thonny.
- 🛠️ Використовувати **покроковий налагоджувач** Thonny для пошуку логічних помилок.

---

## 🧠 Пригадайте!

<div class="card">

Перевірте себе — що виведе цей код і чому?

```python
word = "Python"
print(word[10])
```

А цей?

```python
age = input("Скільки вам років? ")
result = 18 - age
```

</div>

---

## 🐛 Звідки слово "bug"?

<div class="grid-container">
<div class="text-left text-medium-small">

У **1947 році** комп'ютер Harvard Mark II раптово дав збій.

Інженери знайшли причину — справжній метелик 🦋 застряг між контактами реле.

Грейс Хоппер записала в журнал: *«First actual case of bug being found»* і вклеїла комаху.

</div>
<div class="text-left text-medium-small">

<div class="important-to-remember">

**Bug** (жук) — помилка в програмі.

**Debugging** (налагодження) — процес пошуку та виправлення помилок.

</div>

</div>
</div>

---

## 🔴 Три типи помилок Python

<div class="text-medium-small">

| Тип | Коли виникає | Приклад |
|---|---|---|
| **Синтаксична** `SyntaxError` | До запуску програми | Пропущена `:` або `)` |
| **Помилка виконання** (`NameError`, `TypeError`…) | Під час роботи | Ділення на 0, неправильний тип |
| **Логічна** | Програма працює, але результат неправильний | Неправильна формула |

</div>

<div class="important-to-remember">

⚠️ Логічні помилки — найнебезпечніші, бо Python про них **не попереджає**!

</div>

---

## 🔴 SyntaxError — синтаксична помилка

<div class="important-to-remember">

Python **не може запустити** програму — код написаний неправильно.

</div>

<div class="text-medium-small">

```python
# Пропущена дужка:
print("Привіт"

# Пропущена двокрапка:
if x > 5
    print("Більше 5")
```

```
SyntaxError: '(' was never closed
SyntaxError: expected ':'
```

</div>

---

## 🟠 NameError та TypeError

<div class="grid-container">
<div class="text-left text-medium-small">

**NameError** — звернення до змінної, якої не існує.

```python
print(Name)   # Name не визначено
# NameError: name 'Name'
#   is not defined
```

</div>
<div class="text-left text-medium-small">

**TypeError** — неправильний тип даних в операції.

```python
age = input("Вік: ")
result = 18 - age
# TypeError: unsupported
# operand type(s) for -:
# 'int' and 'str'
```

</div>
</div>

---

## 🟡 IndexError та ValueError

<div class="grid-container">
<div class="text-left text-medium-small">

**IndexError** — індекс виходить за межі рядка.

```python
word = "Код"   # індекси: 0,1,2
print(word[4])
# IndexError: string index
#   out of range
```

</div>
<div class="text-left text-medium-small">

**ValueError** — неправильне значення для функції.

```python
number = int("12.5")
# ValueError: invalid literal
#   for int() with base 10: '12.5'

# Правильно:
number = float("12.5")
```

</div>
</div>

---

## 🔍 Як читати повідомлення про помилку

<div class="card text-medium-small">

```
Traceback (most recent call last):
  File "program.py", line 3, in <module>
    result = 18 - age
TypeError: unsupported operand type(s)
    for -: 'int' and 'str'
```

</div>

<div class="text-medium-small">

1. **`line 3`** — номер рядка, де сталася помилка.
2. **`result = 18 - age`** — сам рядок коду.
3. **`TypeError`** — тип помилки.
4. Опис: що саме пішло не так.

</div>

---

## 🛠️ Налагоджувач у Thonny

<div class="text-medium-small">

| Дія | Кнопка | Клавіша |
|---|---|---|
| Запустити в режимі налагодження | ▶ Debug | **Ctrl+F5** |
| Крок через рядок (без входу у функцію) | Step over | **F6** |
| Крок у середину функції | Step into | **F7** |
| Продовжити до кінця | Resume | **F8** |

</div>

<div class="important-to-remember">

💡 Панель **Variables** у Thonny показує поточні значення всіх змінних — дуже корисно для пошуку логічних помилок!

</div>

---

## ⌨️ Практична робота — Завдання 1

<section class="task text-medium-small">

## 🔴 Завдання 1 — SyntaxError (Середній рівень)

Знайди та виправ **2 помилки** у коді:

```python
name = input("Введіть ім'я: "
print("Привіт, " + name)
if len(name) > 5
    print("Довге ім'я!")
```

**Очікуваний результат:** програма вітає користувача та повідомляє, чи довге ім'я.

</section>

---

## ⌨️ Практична робота — Завдання 2

<section class="task text-medium-small">

## 🟠 Завдання 2 — NameError та TypeError (Середній рівень)

Знайди та виправ **2 помилки**:

```python
age = input("Скільки вам років? ")
years_to_18 = 18 - age
print("До повноліття: " + str(years_to_18) + " років")
print("Ваш вік: " + Age)
```

**Очікуваний результат:** програма виводить кількість років до 18 та вік.

</section>

---

## ⌨️ Практична робота — Завдання 3

<section class="task text-medium-small">

## 🟡 Завдання 3 — IndexError та ValueError (Достатній рівень)

Знайди та виправ **2 помилки**:

```python
word = "Код"
print("Перший символ:", word[0])
print("Четвертий символ:", word[4])
number = int("12.5")
print("Число:", number)
```

**Очікуваний результат:** перший символ слова та число 12.5.

</section>

---

## ⌨️ Практична робота — Завдання 4

<section class="task text-medium-small">

## 🔍 Завдання 4 — Логічна помилка (Достатній рівень)

Програма **запускається**, але дає неправильний результат. Використай **налагоджувач** (Ctrl+F5) та панель Variables!

```python
# Має рахувати суму цифр числа 123 → очікується 6
n = 123
hundreds = n % 100
tens = n % 10 // 10
units = n % 10
total = hundreds + tens + units
print("Сума цифр:", total)
```

</section>

---

## ⌨️ Практична робота — Завдання 5 ⭐

<section class="task text-medium-small">

## ⭐ Завдання 5 — Логічна помилка (Високий рівень)

Програма перевіряє паліндром, але працює неправильно. Знайди та виправ помилку:

```python
word = input("Введіть слово: ")
reversed_word = word[-1]
if word == reversed_word:
    print(word, "— це паліндром")
else:
    print(word, "— НЕ паліндром")
```

*Підказка: паліндром — слово, яке однаково читається з обох боків (наприклад: «радар», «racecar»)*

</section>

---

## 👁️ Вправа для очей

<span class="emoji-large">👁️</span>

<div class="card text-medium">

Зробіть паузу від екрану — 1 хвилина:

1. Подивіться у далечінь (у вікно) — 20 секунд.
2. Заплющте очі та виконайте **кругові рухи** очима — 20 секунд.
3. Швидко покліпайте — 20 секунд.

</div>

---

## 🤔 Підсумок уроку

<div class="text-medium-small">

- **Bug / Debugging** — помилка / процес пошуку та виправлення помилок.
- **SyntaxError** — помилка синтаксису, код не запускається.
- **NameError** — звернення до невизначеної змінної.
- **TypeError** — неправильний тип у операції (наприклад, `int - str`).
- **IndexError** — індекс виходить за межі рядка.
- **ValueError** — неправильне значення для функції (наприклад, `int("12.5")`).
- **Логічна помилка** — код працює, але результат неправильний. Для пошуку — налагоджувач **Ctrl+F5**.

</div>

---

## 🏠 Домашнє завдання

<section class="task text-medium-small">

Виконай у 👉 [**onlineide.pro/playground/python**](https://www.onlineide.pro/playground/python)

Доопрацюй завдання, які не встигнув на уроці.

**У зошит запиши:**
- Назви **трьох типів помилок** Python.
- По **одному прикладу** коду для кожного типу.

⭐ *Додатково:* придумай та напиши власну програму з **логічною помилкою**, яку однокласник повинен знайти.

</section>
