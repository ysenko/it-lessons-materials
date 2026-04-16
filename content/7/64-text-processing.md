---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 🖥️ Інформатика | 7 клас
header: 🏫 Урок 64
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

# 📝 Текстові величини в Python та операції над ними

## 🏫 Урок **64**

---

## 🎯 Сьогодні ми дізнаємося

- ℹ️ Що таке тип даних `str` і як створювати рядкові змінні.
- 🔢 Як звертатися до окремих символів рядка за **індексом**.
- 🔧 Що таке **escape-послідовності** та навіщо вони потрібні.
- ✂️ Як "вирізати" частину рядка за допомогою **зрізів**.
- 📏 Як використовувати функції **`len()`**, **`ord()`**, **`chr()`**.

---

## 🧠 Пригадайте!

<div class="card">

На попередніх уроках ми вже знайомилися з типом `str`.

- Яка функція перетворює число на рядок? → `str()`
- Що виведе `type(42)`? → `<class 'int'>`
- Що виведе `type("42")`? → `<class 'str'>`
- Чи можна скласти число та рядок? → ні, буде помилка!

</div>

---

## 📦 Тип даних `str`

<div class="important-to-remember">

**Рядок (str)** — це послідовність символів, записана в **одинарних**, **подвійних** або **потрійних** лапках.

</div>

<div class="text-medium-small">

```python
name = "Аліса"
city = 'Київ'
poem = """Реве та стогне
Дніпр широкий"""

print(type(name))  # <class 'str'>
```

</div>

---

## ➕ Операції з рядками

<div class="text-medium">

| Операція | Приклад | Результат |
|:---|:---|:---|
| Конкатенація `+` | `"Привіт" + " світ"` | `"Привіт світ"` |
| Повторення `*` | `"ха" * 3` | `"хахаха"` |

</div>

<div class="text-medium-small">

```python
name = "Аліса"
greeting = "Привіт, " + name + "!"
print(greeting)   # Привіт, Аліса!
print("=" * 20)   # ====================
```

</div>

---

## 🔢 Індекси в рядках

<div class="important-to-remember">

Кожен символ рядка має **індекс** — порядковий номер, що починається з **0**. Від'ємні індекси відраховуються з **кінця**.

</div>

<div class="text-medium-small">

```
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

```python
s = "Python"
print(s[0])   # P   (перший символ)
print(s[-1])  # n   (останній символ)
print(s[2])   # t
```

</div>

---

## 🔢 Індекси — практика

<div class="text-medium-small">

```python
word = "Інформатика"

print(word[0])    # І  — перший символ
print(word[-1])   # а  — останній символ
print(word[6])    # а  — сьомий символ (індекс 6)
```

</div>

<div class="important-to-remember">

⚠️ Якщо вказати індекс, якого не існує (наприклад `word[100]`), Python видасть помилку `IndexError`.

</div>

---

## 🔤 Escape-послідовності

<div class="card">

**Escape-послідовність** — спеціальна комбінація символів, що починається з `\` і позначає символ, який не можна написати звичайним чином.

</div>

<div class="text-medium-small">

| Послідовність | Значення |
|:---:|:---|
| `\n` | Новий рядок |
| `\t` | Табуляція |
| `\'` | Одинарна лапка |
| `\"` | Подвійна лапка |
| `\\` | Зворотний слеш |

</div>

---

## 🔤 Escape-послідовності — приклади

<div class="text-medium-small">

```python
# \n — перенос рядка
print("Рядок 1\nРядок 2")
# Рядок 1
# Рядок 2

# \t — табуляція
print("Ім'я:\tАліса")
# Ім'я:   Аліса

# \" — лапки всередині рядка
print("Він сказав: \"Привіт!\"")
# Він сказав: "Привіт!"

# \\ — зворотний слеш (наприклад, для шляхів Windows)
print("C:\\Users\\User\\Desktop")
# C:\Users\User\Desktop
```

</div>

---

## ✂️ Зрізи (Slices)

<div class="important-to-remember">

**Зріз** дозволяє отримати частину рядка.
Синтаксис: `рядок[початок : кінець : крок]`
Символ на позиції `кінець` **не включається**.

</div>

<div class="text-medium-small">

```python
s = "Інформатика"
#    0123456789...

print(s[0:6])   # Інформ  (символи 0,1,2,3,4,5)
print(s[6:])    # атика   (від 6 до кінця)
print(s[:6])    # Інформ  (від початку до 6)
```

</div>

---

## ✂️ Зрізи — крок та реверс

<div class="text-medium-small">

```python
s = "Інформатика"

# Крок 2 — кожен другий символ
print(s[::2])    # Іфрмтк

# Від'ємний крок — рядок навпаки
print(s[::-1])   # акитамрофнІ

# Комбінація: кожен другий символ навпаки
print(s[::-2])   # ктмрфІ
```

</div>

<div class="card">

💡 `s[::-1]` — найпростіший спосіб перевернути рядок у Python!

</div>

---

## 📏 Функція `len()`

<div class="card">

**`len(рядок)`** повертає **кількість символів** у рядку (довжину рядка).

</div>

<div class="text-medium-small">

```python
print(len("Привіт"))       # 6
print(len("Python"))       # 6
print(len(""))             # 0  (порожній рядок)
print(len("Привіт світ"))  # 11 (пробіл теж символ!)

name = "Аліса"
# Останній символ через len()
print(name[len(name) - 1])  # а
# Те саме, але простіше:
print(name[-1])              # а
```

</div>

---

## 🔡 Функції `ord()` та `chr()`

<div class="grid-container">
<div class="text-left text-medium-small">

**`ord(символ)`** — повертає числовий **Unicode-код** символу.

```python
print(ord("A"))   # 65
print(ord("a"))   # 97
print(ord("А"))   # 1040
print(ord("а"))   # 1072
print(ord("0"))   # 48
```

</div>
<div class="text-left text-medium-small">

**`chr(число)`** — повертає **символ** за його кодом.

```python
print(chr(65))    # A
print(chr(97))    # a
print(chr(1040))  # А
print(chr(1072))  # а
```

</div>
</div>

---

## 🔡 `ord()` + `chr()` — разом

<div class="card">

`ord()` і `chr()` — взаємообернені функції. Разом вони дозволяють "пересуватися" по алфавіту.

</div>

<div class="text-medium-small">

```python
letter = "А"
print(chr(ord(letter) + 1))   # Б  (наступна літера)
print(chr(ord(letter) - 1))   # @  (попередній символ у Unicode)

# Перевірка: ord і chr скасовують одне одного
print(chr(ord("Щ")))          # Щ
```

</div>

---

## ⌨️ Практичне завдання

<section class="task text-medium">

## ⌨️ Завдання в Thonny

**Завдання 1 (обов'язкове):** Напиши програму, яка:
1. Зберігає введене ім'я та прізвище у змінних `name` і `surname`.
2. Виводить першу літеру імені та останню літеру прізвища.
3. Виводить ім'я в зворотному порядку (зріз `[::-1]`).
4. Виводить кількість символів у повному імені (`name + " " + surname`).

</section>

---

## 🔐 Додаткове завдання — Шифрувальник

<section class="task text-medium">

## 🔐 Завдання 2 (додаткове)

**Шифрувальник Цезаря (спрощений)**

1. Створи змінну і надай їй значеннчя: `message = "HELLO"`
2. Для кожної літери виведи символ з кодом на 1 більше:
   ```python
   print(chr(ord(message[0]) + 1))  # I
   print(chr(ord(message[1]) + 1))  # F
   # ... і так далі для кожної літери
   ```
3. Яке "зашифроване" слово вийшло?

</section>

---

## 🤔 Підсумок уроку

<div class="text-medium-small">

- **`str`** — тип даних для тексту. Записується в одинарних, подвійних або потрійних лапках.
- **Індекс** — номер символу в рядку (починається з `0`, від'ємні — з кінця).
- **Escape-послідовності** — спеціальні символи: `\n`, `\t`, `\"`, `\\`.
- **Зріз** `[початок:кінець:крок]` — отримати частину рядка.
- **`len(s)`** — довжина рядка.
- **`ord(c)`** — Unicode-код символу.
- **`chr(n)`** — символ за кодом.

</div>

---

## 🏠 Домашнє завдання

<div class="task text-medium-small">

Виконай у 👉 [**onlineide.pro/playground/python**](https://www.onlineide.pro/playground/python)

**Програма «Аналізатор тексту»:**
1. Введи текст з клавіатури: `text = input("Введіть слово або фразу: ")`
2. Виведи **довжину** рядка, **перший** та **останній** символи, рядок **навпаки**.
3. Виведи **Unicode-коди** першого та останнього символів.
4. ⭐ *Додатково:* виведи рядок, де перший символ замінено на `chr(ord(text[0]) + 1)`.

</div>
