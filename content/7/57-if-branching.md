---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 57
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

# 🔀 Розгалужені алгоритми в Python. Оператор `if`

## 🏫 Урок **57**

---

## 🎯 Сьогодні ми дізнаємося

- 🔀 Що таке **оператор `if`** та навіщо він потрібен.
- 📌 Три форми: **`if`**, **`if...else`**, **`if...elif...else`**.
- ⚠️ Як **не допускати** типових помилок у розгалуженнях.
- ⌨️ Як **самостійно писати** програми з розгалуженнями.

---

## 🧠 Пригадайте!

<div class="card">

Що виведе цей код?

```python
age = 16
print(age >= 18)
print(not False)
print(bool(""))
```

Яка різниця між `=` та `==`?

</div>

---

## 💡 Навіщо потрібен `if`?

<div class="important-to-remember">

Ми вміємо **порівнювати** значення і отримувати `True` / `False`.

Але як змусити програму **робити різні дії** залежно від результату?

</div>

<div class="card text-medium-small">

**Без `if`:**
```python
age = int(input("Введіть вік: "))
print(age >= 18)   # просто виведе True або False
```

**З `if`:**
```python
if age >= 18:
    print("Вхід дозволено ✅")
```

</div>

---

## 🔀 Форма 1: простий `if`

<div class="important-to-remember">

```python
if умова:
    # виконується лише якщо умова True
```

</div>

<div class="text-medium-small">

- Після `if` — обов'язкова **двокрапка `:`**
- Тіло — з **відступом** (4 пробіли або Tab)
- Якщо умова `False` — блок **пропускається**

```python
age = int(input("Введіть вік: "))
if age >= 18:
    print("Ви повнолітній! 🎉")
print("Програма завершена.")
```

</div>

---

## 🔀 Форма 1: `if` — схема

<div class="grid-container">
<div class="text-left text-medium-small">

**Умова `True` (вік = 20):**
```
Введіть вік: 20
Ви повнолітній! 🎉
Програма завершена.
```

**Умова `False` (вік = 15):**
```
Введіть вік: 15
Програма завершена.
```

</div>
<div class="text-left text-medium-small">

**Алгоритм:**

```
age >= 18?
   │
 Так ──► print("Ви повнолітній!")
   │
 Ні  ──► (пропустити)
   │
   ▼
print("Програма завершена.")
```

</div>
</div>

---

## 🔀 Форма 2: `if...else`

<div class="important-to-remember">

```python
if умова:
    # якщо True
else:
    # якщо False
```

</div>

<div class="card text-medium-small">

**Приклад — парне чи непарне?**

```python
num = int(input("Введіть число: "))
if num % 2 == 0:
    print("Число парне ✅")
else:
    print("Число непарне ❌")
```

`%` — остача від ділення. Якщо остача 0 — число парне.

</div>

---

## 🔀 Форма 2: `if...else` — схема

<div class="grid-container">
<div class="text-left text-medium-small">

**num = 4:**
```
Введіть число: 4
Число парне ✅
```

**num = 7:**
```
Введіть число: 7
Число непарне ❌
```

</div>
<div class="text-left text-medium-small">

**Алгоритм:**

```
num % 2 == 0?
   │
 Так ──► "парне"
   │
 Ні  ──► "непарне"
```

Виконується **рівно один** з двох блоків.

</div>
</div>

---

## 🔀 Форма 3: `if...elif...else`

<div class="important-to-remember">

```python
if умова_1:
    # якщо умова_1 True
elif умова_2:
    # якщо умова_2 True (умова_1 вже False)
elif умова_3:
    # якщо умова_3 True (попередні False)
else:
    # жодна умова не виконалась
```

</div>

<div class="text-medium-small">

`elif` = «else if» — ще одна умова. Блоків `elif` може бути скільки завгодно.

</div>

---

## 🔀 Форма 3: приклад — оцінка за балами

<div class="text-medium-small">

```python
score = int(input("Введіть бал (0-100): "))
if score >= 90:
    print("Відмінно 🌟")
elif score >= 75:
    print("Добре 👍")
elif score >= 60:
    print("Задовільно 😐")
else:
    print("Незадовільно 😢")
```

</div>

<div class="important-to-remember">

⚡ Умови перевіряються **зверху вниз**. Виконується **лише перший збіг** — решта ігноруються!

</div>

---

## 🔀 Форма 3: порядок умов важливий!

<div class="grid-container">
<div class="text-left text-medium-small">

**Правильно ✅**
```python
if score >= 90:
    print("Відмінно")
elif score >= 75:
    print("Добре")
elif score >= 60:
    print("Задовільно")
else:
    print("Незадовільно")
```
score = 95 → «Відмінно»

</div>
<div class="text-left text-medium-small">

**Неправильно ❌**
```python
if score >= 60:
    print("Задовільно")
elif score >= 75:
    print("Добре")
elif score >= 90:
    print("Відмінно")
```
score = 95 → «Задовільно» 😱

</div>
</div>

---

## ⚠️ Типові помилки

<div class="text-medium-small">

| Помилка | Тип помилки | Виправлення |
|---|---|---|
| `if age = 18:` | `SyntaxError` | `if age == 18:` |
| Немає `:` після умови | `SyntaxError` | Додати `:` |
| Немає відступу в тілі | `IndentationError` | 4 пробіли або Tab |
| `elif` без `if` | `SyntaxError` | Перевірити структуру |

</div>

<div class="card text-medium-small">

```python
# ❌ Неправильно:
if x = 5       # SyntaxError: = замість ==
    print(x)   # IndentationError: немає відступу

# ✅ Правильно:
if x == 5:
    print(x)
```

</div>

---

## ⌨️ Практична робота — Завдання 1

<section class="task text-medium-small">

## 🔢 Завдання 1 — Парне чи непарне?

Напиши програму, яка:
1. Запитує ціле число: `num = int(input("Введіть число: "))`.
2. Виводить **«Парне»**, якщо число ділиться на 2 без остачі.
3. Виводить **«Непарне»** — інакше.

**Підказка:** `num % 2 == 0` → число парне.

</section>

---

## ⌨️ Практична робота — Завдання 2

<section class="task text-medium-small">

## 🍂 Завдання 2 — Пори року

Напиши програму, яка запитує **номер місяця (1–12)** і виводить пору року:

- **Зима:** 12, 1, 2
- **Весна:** 3, 4, 5
- **Літо:** 6, 7, 8
- **Осінь:** 9, 10, 11
- Інше число → **«Некоректний місяць»**

**Підказка:** `month == 12 or month == 1 or month == 2`

</section>

---

## ⌨️ Практична робота — Завдання 3 ⭐

<section class="task text-medium-small">

## 🛒 Завдання 3 ⭐ — Калькулятор знижок

Напиши програму: запитує суму покупки та виводить знижку і фінальну ціну:

| Сума | Знижка |
|---|---|
| від 5000 грн | 15% |
| від 2000 грн | 10% |
| від 1000 грн | 5% |
| менше 1000 грн | 0% |

Вивести: розмір знижки в грн та суму до сплати.

</section>

---

## 🤔 Підсумок уроку

<div class="text-medium-small">

- **`if умова:`** — виконується, якщо умова `True`; інакше — пропускається.
- **`if...else`** — два шляхи: один виконується завжди.
- **`if...elif...else`** — багато шляхів; перевірка **зверху вниз**, виконується **лише перший збіг**.
- **Обов'язково:** двокрапка `:` після умови та **відступ** у тілі.
- **Типові помилки:** `=` замість `==`, відсутній відступ, відсутня `:`.

</div>

---

## 🏠 Домашнє завдання

<section class="task text-medium-small">

📖 **Опрацювати підручник с. 237–242.**

Виконати у 👉 [**onlineide.pro/playground/python**](https://www.onlineide.pro/playground/python)

**Програма «Знак числа»:**

1. Ввести ціле число: `num = int(input("Введіть число: "))`.
2. Вивести результат:
   - `«Додатне»` — якщо число більше 0.
   - `«Від'ємне»` — якщо число менше 0.
   - `«Нуль»` — якщо число дорівнює 0.

</section>
