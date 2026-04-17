---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 56
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

# ⚖️ Порівняння значень величин. Логічні величини

## 🏫 Урок **56**

---

## 🎯 Сьогодні ми дізнаємося

- ✅ Що таке **логічний тип даних `bool`**.
- ⚖️ Як використовувати **оператори порівняння** для чисел і рядків.
- 🔗 Як поєднувати умови за допомогою **`and`, `or`, `not`**.
- 🔄 Як **перетворювати** логічні значення в числа та рядки.

---

## 🧠 Пригадайте!

<div class="card">

Що виведе цей код?

```python
age = input("Скільки вам років? ")
print(type(age))
```

А якщо написати `print(type(18))`?

Яка різниця між `=` і `==` у Python?

</div>

---

## ✅ Тип даних `bool`

<div class="important-to-remember">

**`bool`** — логічний тип даних. Може приймати лише **два значення**: `True` (істина) або `False` (хибність).

</div>

<div class="text-medium-small">

```python
print(type(True))    # <class 'bool'>
print(type(False))   # <class 'bool'>

# Результат порівняння — завжди bool:
print(5 > 3)    # True
print(5 < 3)    # False
```

</div>

---

## ⚖️ Оператори порівняння

<div class="text-medium-small">

| Оператор | Значення | Приклад | Результат |
|:---:|:---|:---|:---:|
| `==` | Рівно | `5 == 5` | `True` |
| `!=` | Не рівно | `5 != 3` | `True` |
| `>` | Більше | `7 > 10` | `False` |
| `<` | Менше | `3 < 8` | `True` |
| `>=` | Більше або рівно | `5 >= 5` | `True` |
| `<=` | Менше або рівно | `4 <= 3` | `False` |

</div>

---

## ⚖️ Оператори порівняння — практика

<div class="card text-medium-small">

```python
age = 16
print(age >= 18)    # False — ще не повнолітній

score = 90
print(score == 100)  # False
print(score >= 60)   # True
```

</div>

<div class="important-to-remember">

⚠️ Не плутайте `=` (присвоєння) та `==` (порівняння)!

`age = 16` — записуємо значення у змінну.
`age == 16` — порівнюємо і отримуємо `True` або `False`.

</div>

---

## 🔤 Порівняння рядків

<div class="card text-medium-small">

Python порівнює рядки **за Unicode-кодами** символів (лексикографічно — як у словнику).

```python
print("apple" < "banana")   # True  (a < b за алфавітом)
print("A" < "a")            # True  (A=65, a=97 в Unicode)
print("5" == 5)             # False (рядок ≠ число!)
```

</div>

<div class="important-to-remember">

💡 `"5" == 5` → **`False`**: Python не перетворює типи автоматично при порівнянні!

</div>

---

## 🔗 Логічні оператори

<div class="important-to-remember">

Логічні оператори дозволяють **поєднувати кілька умов** в одне вираження.

</div>

<div class="text-medium-small">

| Оператор | Значення | Коли `True`? |
|:---:|:---|:---|
| `and` | І | Коли **обидві** умови `True` |
| `or` | АБО | Коли **хоча б одна** умова `True` |
| `not` | НЕ | Інвертує: `True` → `False`, `False` → `True` |

</div>

---

## 🔗 `and` — "І"

<div class="card text-medium-small">

**Аналогія:** «Я піду гуляти, якщо закінчу уроки **і** надворі не буде дощу.»

Обидві умови мають бути виконані.

```python
temp = 25
print(temp >= 20 and temp <= 30)  # True  — комфортно
print(temp >= 20 and temp <= 24)  # False — хоч одна хибна
```

</div>

---

## 🔗 `or` — "АБО"

<div class="card text-medium-small">

**Аналогія:** «Ми підемо в кіно **або** в театр — будь-що.»

Достатньо однієї виконаної умови.

```python
temp = -5
print(temp < 0 or temp > 35)   # True  — мороз!
print(temp > 0 or temp > 35)   # False — жодна не виконана
```

</div>

---

## 🔗 `not` — "НЕ"

<div class="card text-medium-small">

**Аналогія:** «Якщо **НЕ** дощ — беру велосипед.»

Інвертує (перевертає) логічне значення.

```python
is_raining = False
print(not is_raining)    # True  — дощу немає, їдемо!

print(not True)          # False
print(not False)         # True
```

</div>

---

## 📊 Таблиця істинності

<div class="text-medium-small">

| `A` | `B` | `A and B` | `A or B` | `not A` |
|:---:|:---:|:---:|:---:|:---:|
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

</div>

---

## 🔄 `bool()` — перетворення в логічний тип

<div class="important-to-remember">

Будь-яке значення можна перетворити в `bool`. **"Порожні" і "нульові" значення** → `False`, усе інше → `True`.

</div>

<div class="text-medium-small">

```python
print(bool(0))       # False  ← нуль
print(bool(0.0))     # False  ← нульове дробове
print(bool(""))      # False  ← порожній рядок

print(bool(42))      # True
print(bool("False")) # True  ← НЕ порожній рядок!
print(bool(" "))     # True  ← пробіл — не порожній!
```

</div>

---

## 🔢 `bool` ↔ числа та рядки

<div class="grid-container">
<div class="text-left text-medium-small">

**`int(bool)`** — `True` = `1`, `False` = `0`

```python
print(int(True))     # 1
print(int(False))    # 0

# Можна навіть рахувати!
print(True + True)   # 2
print(True + False)  # 1
```

</div>
<div class="text-left text-medium-small">

**`str(bool)`** — перетворює на текст

```python
print(str(True))     # 'True'
print(str(False))    # 'False'

# Виведення рядком
result = True
print("Результат: " + str(result))
# Результат: True
```

</div>
</div>

---

## ⌨️ Практична робота — Завдання 1

<section class="task text-medium-small">

## 📝 Завдання 1 — Передбачте результат

Запишіть у зошит, що, на вашу думку, виведе кожен рядок. Потім виконайте в Thonny і перевірте:

```python
print(10 > 5)
print(3 == 3.0)
print("abc" == "ABC")
print("a" < "b")
print("5" == 5)
print(bool(""))
print(bool("0"))
```

</section>

---

## ⌨️ Практична робота — Завдання 2

<section class="task text-medium-small">

## 🌡️ Завдання 2 — Перевірка температури

Напиши програму, яка:
1. Запитує температуру повітря (`float(input(...))`).
2. Виводить `True`, якщо температура від 18 до 26 градусів (комфортна).
3. Виводить `True`, якщо температура нижче 0 або вище 35 (екстремальна).

```python
temp = float(input("Введіть температуру: "))
print("Комфортна:", temp >= 18 and temp <= 26)
print("Екстремальна:", temp < 0 or temp > 35)
```

</section>

---

## ⌨️ Практична робота — Завдання 3 ⭐

<section class="task text-medium-small">

## ⭐ Завдання 3 — Пошук «хибних» значень

Відкрий Thonny та перевір кожне зі значень через `bool()`. Визнач, які з них **«хибні»** (дають `False`):

```
0,  0.0,  "",  "0",  "False",  -1,  " "
```

Зверни увагу: які з них числа, а які — рядки в лапках?

```python
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool("0"))
# ... і так далі
```

Запиши у зошит: які значення виявилися `False`?

</section>

---

## 🤔 Підсумок уроку

<div class="text-medium-small">

- **`bool`** — логічний тип, лише `True` або `False`.
- **Оператори порівняння:** `==`, `!=`, `>`, `<`, `>=`, `<=` — повертають `bool`.
- **Рядки** порівнюються за Unicode (лексикографічно); `"5" == 5` → `False`.
- **`and`** — істина, коли **обидві** умови виконані.
- **`or`** — істина, коли **хоча б одна** умова виконана.
- **`not`** — інвертує логічне значення.
- **«Хибні» значення:** `0`, `0.0`, `""` → `False`; усе інше → `True`.
- **`int(True)` = `1`**, **`int(False)` = `0`**.

</div>

---

## 🏠 Домашнє завдання

<section class="task text-medium-small">

Виконай у 👉 [**onlineide.pro/playground/python**](https://www.onlineide.pro/playground/python)

Напиши програму **«Скільки тобі буде років?»**:

1. Введи рік народження: `year = int(input("Рік народження: "))`.
2. Порахуй вік у поточному році (наприклад, 2026): `current_year = 2026; age = current_year - year`.
3. Виведи `True`, якщо вже виповнилося 18 років: `print("Повнолітній:", age >= 18)`.
4. ⭐ *Додатково:* виведи `True`, якщо вік від 7 до 17 (шкільний вік).

</section>
