---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 62
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
    max-width: 100%; /* Ensures the image scales within its space */
    height: auto;
    text-align: center;
    display: flex;
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

# Поняття про модуль в Python. Робота з модулями

## 🏫 Урок **62**

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке модуль у Python.
- 🔧 Як підключати модулі до програми.
- ✏️ Як використовувати стандартні модулі `math`, `random` та `string`.
- 🐍 Закріпимо знання про змінні.

---

## 🧠 Пригадаймо!

<div class="grid-container">
<div class="card">

### Змінні

Як правильно назвати змінну?
* `1_value` ❌
* `my-value` ❌
* `my_value` ✅

</div>
<div class="card">

### Типи даних
Що виведе код?
`print(5 + "5")`
* А) 10
* Б) "55"
* В) Помилку! ✅

</div>
</div>

---

## 🤔 Проблема: як бути точним?

Як обчислити площу кола, якщо нам потрібне точне значення числа $\pi$ (3.14159...)?

Або як змусити Python "підкинути кубик" і видати випадкове число?

Для цього нам потрібні **модулі**! 📦

---

<section class="card">

## 📦 Що таке модуль?

**Модуль** — це файл, який містить готовий програмний код (функції, змінні, константи), і який можна використовувати у своїх програмах.

Це як "коробка з інструментами", яку ви берете з полиці, коли вона вам потрібна.

</section>

---

<section class="important-to-remember">

## 🔧 Як підключити модуль?

Для підключення модуля використовують команду `import`:

```python
import math    # Підключаємо модуль math
import random  # Підключаємо модуль random
```

**Важливо:** зазвичай модулі підключають на самому початку програми.

</section>

---

## 📐 Модуль `math`

Містить математичні функції та константи.

* `math.pi` — число $\pi$.
* `math.sqrt(x)` — квадратний корінь із числа $x$.

```python
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0
```

---

## 🎲 Модуль `random`

Дозволяє працювати з випадковими числами.

* `random.randint(a, b)` — випадкове ціле число в діапазоні від $a$ до $b$ (включно).
* `random.choice(seq)` — випадковий елемент із послідовності (`list`, `string` тощо).

```python
import random

number = random.randint(1, 10)
print("Випало число:", number)

color = random.choice(["червоний", "синій", "зелений"])
print("Випав колір:", color)
```

---

## 🛡️ Модуль `string` та безпека

Окрім `math` та `random`, у Python є модуль `string`, який містить готові набори символів.

- `string.ascii_letters` — усі латинські літери (A-Z, a-z).
- `string.digits` — цифри від 0 до 9.
- `string.punctuation` — знаки пунктуації (!, #, $, %, ...).

Це дуже зручно, коли нам потрібно створити щось випадкове з тексту!

---

## 🔐 Генератор PIN-коду

```python
import random
import string

# Використовуємо тільки цифри
digits = string.digits

# Вибираємо 4 випадкові цифри
d1 = random.choice(digits)
d2 = random.choice(digits)
d3 = random.choice(digits)
d4 = random.choice(digits)

pin = d1 + d2 + d3 + d4

print("Ваш новий PIN-код:", pin)
```

---

<section class="task">

## 🧩 Завдання-виклик: від PIN до пароля!

Спробуйте внести зміни у програму:

1. **Складніший пароль:** Змініть `digits` на `string.ascii_letters`, щоб замість цифр були літери.
2. **Довжина:** Додайте змінні `d5` та `d6`, щоб PIN-код або пароль мав 6 символів.
3. **Мікс:** Спробуйте поєднати `string.digits + string.ascii_letters`. Що вийде?

</section>

---

## 🏠 Домашнє завдання: «Математичний помічник»

<div class="task text-medium-small">

Створіть програму-калькулятор, яка допоможе з математикою!

**Інструкція до виконання:**

1. Імпортуйте модуль `math` за допомогою `import math`.
2. Запитайте у користувача радіус кола за допомогою `input`.
3. Перетворіть введене значення у дробове число (`float`).
4. Обчисліть площу кола: $S = math.pi \cdot r^2$.
5. Знайдіть квадратний корінь із введеного радіуса за допомогою `math.sqrt()`.
6. Виведіть результати на екран.

</div>

---

## 💻 Де писати код?

Якщо у вас вдома не встановлено Python, скористайтеся онлайн-редактором:

👉 [**Online Python IDE**](https://www.onlineide.pro/playground/python)

**Як показати роботу?**

- Зробіть фото або знімок екрана з **кодом** та **результатами виконання програми**.
- Будьте готові пояснити свою **програму** в класі.
