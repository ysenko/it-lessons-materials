---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 51
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

# 🐍 Робота зі змінними: Введення та Обчислення

## 🏫 Урок **51**

---

## 🎯 Сьогодні ми навчимося:

- 🏷️ Правильно вибирати імена для змінних.
- ⚙️ Швидко створювати багато змінних.
- 🗣️ «Спілкуватися» з програмою через клавіатуру.
- 🧮 Виконувати математичні операції з введеними даними.

---

## ⚡ Секрети присвоєння

<div class="important-to-remember text-medium-small">

- `a = 1` - записуємо значення у змінну
- `b = c = d = 10` — однакове значення для багатьох змінних.
- `x, y = 1, 2` — кілька значень одним рядком.

</div>

<div class="task text-medium">

**Практика:** Скопіюйте код і виконайте його.
Який результат ви бачите? Поясніть чому.

```python
a = 1
b = c = d = "Привіт!"

print(a, b, c, d)
```

</div>

---

## 🏷️ Як називати змінні?

<div class="grid-container text-medium-small">
  <div class="grid-item">

### 🚫 Правила (Обов'язково)
- Тільки латинські літери, цифри та `_`.
- Не можна починати з цифри.
- Мають значення великі/малі літери (`Age` $\neq$ `age`).
  </div>
  <div class="grid-item">

### 💡 Поради (Для зручності)
- Називайте змінні за змістом: `score`, `user_name` замість `s`, `n`.
- Використовуйте `snake_case`: слова з маленької літери через `_`.
  </div>
</div>

---

## 🎤 Команда input()

<section class="text-medium">

Зустрівши цю команду, програма зупиняється і чекає, поки ви введете дані.

<div class="important-to-remember">

**Важливо:** `input()` завжди повертає **ТЕКСТ** (тип `str`), навіть якщо ви ввели цифри.

</div>

<div class="task">

**Практика:** Скопіюйте та виконайте її.

```python
city = input("В якому місті ти живеш? ")
print("О! Я чув, що", city, "- це чудове місто!")
```

</div>
</section>

---

## 🧮 Математика в Python

<section class="text-medium">

Щоб рахувати, треба перетворити текст на число: `int(input())`, або `float(input())` для дробових чисел.

| Операція | Символ |
| :--- | :--- |
| Додавання / Віднімання | `+` / `-` |
| Множення / Ділення | `*` / `/` |
| Ціла частина від ділення | `//` |
| Остача від ділення | `%` |
| Піднесення до степеня | `**` |

</section>

---

## 📦 Ціла частина та остача

<div class="grid-container">
  <div class="grid-item">

### `//` Ціла частина
Скільки разів число вміщується повністю.
`17 // 5` $\rightarrow$ **3**
  </div>
  <div class="grid-item">

### `%` Остача
Те, що залишилося після ділення.
`17 % 5` $\rightarrow$ **2**
  </div>
</div>

<div class="task">

**Перевірка:** Що виведе `10 % 3`?

</div>

---

## 💻 Рахуємо разом

<div class="task">

**Завдання:** Скопіюйте код. Змініть його так, щоб програма запитувала два числа і додавала їх.

</div>

```python
num1 = int(input("Введіть число: "))
result = num1 * num1
print("Квадрат цього числа =", result)
```

---

## 🏠 Домашнє завдання

<div class="task">

1. Напишіть у зошиті або в редакторі код для програми:

   1. Запитує сторону квадрата `a`.
   2. Рахує площу за формулою $S = a \times a$ (або $a^2$).
   3. Виводить результат на екран.
2. Запитайте в ШІ як працюють оператори +=, -=, *=, /= в мові Python. Підготуйтеся розповісти про це в класі.

</div>
