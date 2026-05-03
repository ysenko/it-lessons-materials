---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 60
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

# 🔄 Цикл `for` та функція `range()`

## 🏫 Урок **60**

---

## 🎯 Сьогодні ми дізнаємося

- 🔁 Як працює цикл **`for`** і чим він відрізняється від `while`.
- 📐 Що таке функція **`range()`** та як її використовувати.
- ⚖️ Коли краще обирати `for`, а коли `while`.
- ⌨️ Як самостійно писати програми з `for` та уникати типових помилок.

---

## 🧠 Перевірка домашнього завдання

<div class="card text-medium-small">

**Програма «Зворотний відлік»** — хто покаже свій код?

```python
n = int(input("Введіть N: "))
while n >= 1:
    print(n)
    n = n - 1
print("Старт! 🚀")
```

</div>

<div class="important-to-remember text-medium-small">

Перевіряємо: ✅ умова правильна? ✅ лічильник оновлюється? ✅ «Старт!» після циклу?

</div>

---

## 🧠 Бліц: цикл `while`

<div class="text-medium-small">

1. Яка різниця між `while True:` і `while умова:`?

2. Для чого потрібен `break`?

3. Що виведе цей код?
```python
count = 3
while count > 0:
    print(count)
    count = count - 1
else:
    print("Старт!")
```

</div>

---

## 💡 Навіщо потрібен `for`?

<div class="grid-container">
<div class="text-left text-medium-small">

**`while` — потрібно вести лічильник вручну:**
```python
count = 1
while count <= 5:
    print(count)
    count = count + 1
```
Три змінні, три рядки на керування циклом.

</div>
<div class="text-left text-medium-small">

**`for` — лічильник автоматичний:**
```python
for count in range(1, 6):
    print(count)
```
Коротше. Читабельніше. Результат однаковий! 🎉

</div>
</div>

<div class="important-to-remember text-medium-small">

`for` зручний, коли **кількість повторень відома заздалегідь**.

</div>

---

## 🔄 Синтаксис циклу `for`

<div class="important-to-remember">

```python
for змінна in послідовність:
    # тіло циклу
    # (виконується для кожного елемента)
```

</div>

<div class="grid-container">
<div class="text-left text-medium-small">

- `змінна` — отримує значення кожного елемента по черзі
- `послідовність` — рядок, список або результат `range()`
- Тіло — обов'язково з **відступом** (Tab або 4 пробіли)
- Цикл завершується **автоматично**, коли елементи вичерпано

</div>
<div class="text-left text-medium-small">

Приклад — перебір рядка:
```python
for letter in "Python":
    print(letter)
```
```
P  y  t  h  o  n
```
Кожна ітерація — наступний символ.

</div>
</div>

---

## 📐 Функція `range()`

<div class="card text-medium-small">

`range()` — генерує послідовність цілих чисел для циклу `for`.

</div>

<div class="text-medium-small">

| Форма | Що генерує | Результат |
|---|---|---|
| `range(stop)` | від 0 до stop–1 | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, stop)` | від start до stop–1 | `range(1, 6)` → 1, 2, 3, 4, 5 |
| `range(start, stop, step)` | від start, крок step | `range(0, 10, 2)` → 0, 2, 4, 6, 8 |

</div>

<div class="important-to-remember text-medium-small">

⚠️ Кінцеве значення (`stop`) **не включається** до послідовності!

</div>

---

## 📐 `range()` — приклади

<div class="text-medium-small">

```python
# Числа від 1 до 5:
for i in range(1, 6):
    print(i)          # 1 2 3 4 5
```

```python
# Парні числа від 0 до 10:
for i in range(0, 11, 2):
    print(i)          # 0 2 4 6 8 10
```

</div>

---

## ⚖️ `for` чи `while`?

<div class="important-to-remember text-medium-small">

**`for`** — кількість повторень **відома** наперед.
**`while`** — повторюємо, **доки виконується умова**.

</div>

<div class="grid-container">
<div class="text-left text-medium-small">

✅ **`for`** — таблиця множення (рівно 10 рядків):
```python
for i in range(1, 11):
    print(f"3 × {i} = {3*i}")
```

</div>
<div class="text-left text-medium-small">

✅ **`while`** — «Вгадай число» (кількість спроб невідома):
```python
secret = 7
guess = int(input("Введи: "))
while guess != secret:
    guess = int(input("Ще раз: "))
```

</div>
</div>

---

## ⌨️ Практична робота — Завдання 1

<section class="task text-medium-small">

## 🔢 Завдання 1 — Таблиця множення

Напиши програму, яка:
1. Запитує число від 1 до 9: `n = int(input("Введіть число: "))`.
2. За допомогою **`for`** та **`range()`** виводить таблицю множення для цього числа (від ×1 до ×10).

**Приклад виводу для n = 3:**
```
3 × 1 = 3
3 × 2 = 6
...
3 × 10 = 30
```

</section>

---

## ⌨️ Практична робота — Завдання 2

<section class="task text-medium-small">

## ➕ Завдання 2 — Сума парних чисел

Напиши програму:
1. Запитати натуральне число N.
2. За допомогою `for` та `range()` обчислити суму всіх парних чисел від 0 до N включно.
3. Вивести результат.

**Приклад виводу для N = 10:**
```
Сума парних від 0 до 10 = 30
```

**Підказка:** `range(0, N+1, 2)` — крок 2, починаючи з 0.

</section>

---

## ⌨️ Практична робота — Завдання 3 ⭐

<section class="task text-medium-small">

## 🌟 Завдання 3 ⭐ — Ромб зірочок

Напиши програму, яка запитує непарне число N і виводить «ромб» зі зірочок.

**Приклад для N = 5:**
```
*
***
*****
***
*
```

**Підказка:** два цикли:
- верхня половина: `for i in range(1, N+1, 2)`
- нижня половина: `for i in range(N-2, 0, -2)`

</section>

---

## 🤔 Підсумок уроку

<div class="text-medium-small">

- 🔄 **`for змінна in послідовність:`** — повторює тіло для кожного елемента автоматично.
- 📐 **`range(1, 6)`** → 1, 2, 3, 4, 5 &nbsp;|&nbsp; **`range(0, 11, 2)`** → 0, 2, 4, 6, 8, 10
- ⚠️ Кінцеве значення `range()` **не включається**.
- ⚖️ **`for`** — кількість повторень відома; **`while`** — залежить від умови.

</div>

---

## 🏠 Домашнє завдання

<section class="task text-medium-small">

📖 **Опрацювати підручник** (розділ про цикл `for` та `range()`).

Виконати у 👉 [**onlineide.pro/playground/python**](https://www.onlineide.pro/playground/python)

**Програма «Факторіал»:**
1. Запитати натуральне число N: `n = int(input("Введіть N: "))`.
2. За допомогою `for` обчислити N! (добуток чисел від 1 до N).
3. Вивести результат. Приклад: N=5 → `5! = 120`.

**За бажанням ⭐ — «Числа Фібоначчі»:**
- Запитати кількість N, вивести перші N чисел послідовності Фібоначчі: 0, 1, 1, 2, 3, 5, 8...

</section>
